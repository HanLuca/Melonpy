from melonapi import scrapeMelon
import json, time, requests
from bs4 import BeautifulSoup
from selenium import webdriver

start = time.time()

chartKeys = ['ranking', 'name', 'artists', 'songId', 'albumId']

options = webdriver.ChromeOptions()

options.add_argument("headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

def loadMelonChart():
	driver.get("https://www.melon.com/chart/index.htm")
	soup = BeautifulSoup(driver.page_source, 'html.parser')

	MelonChart = json.loads(scrapeMelon.getList('LIVE').decode())
	MelonChartList = [[0, 'MelonChart']]

	for i in range(1, 101):
		songLikes = soup.find_all("tr", {"data-song-no": True})[i - 1].find("button", {"class": "button_etc like"}).getText().split()[2]

		MelonChartList.append(
			[MelonChart[str(i)][c] for c in chartKeys] +
			[songLikes]
		)

	print(MelonChartList)
	return MelonChartList