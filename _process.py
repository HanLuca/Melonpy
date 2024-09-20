from melonapi import scrapeMelon
import json, time, requests, datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from collections import Counter
from flask import request

chartKeys = ['ranking', 'name', 'artists', 'songId', 'albumId']

options = webdriver.ChromeOptions()

options.add_argument("headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

def loadMelonChart():
	driver.get("https://www.melon.com/chart/index.htm")
	time.sleep(2)
	soup = BeautifulSoup(driver.page_source, 'html.parser')

	MelonChart = json.loads(scrapeMelon.getList('LIVE').decode())
	MelonChartList = [[0, 'MelonChart']]

	for i in range(1, 101):
		songLikes = soup.find_all("tr", {"data-song-no": True})[i - 1].find("button", {"class": "button_etc like"}).getText().split()[2]

		MelonChartList.append(
			[MelonChart[str(i)][c] for c in chartKeys] +
			[songLikes]
		)

	return MelonChartList

def loadArtistsChart(melonChart):
	artistsChart = {}
	artists = [melonChart[i][2] for i in range(1, len(melonChart))]

	artistsChart['artistsChartName'] = [artist for artist, count in Counter(artists).most_common()]
	artistsChart['artistsChartCount'] = [count for artist, count in Counter(artists).most_common()]
	
	return artistsChart

def loggingData(string):
	with open('log.txt', 'a') as log:
		log.write(f"[{datetime.date.today()}] [{request.remote_addr}] :: {string}\n")