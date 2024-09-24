# SongDetailList = [Ranking, SongName, Artists, SongId, AlbumId, Likes]

from melonapi import scrapeMelon
from flask import Flask, request, render_template, redirect, session, url_for
import json, datetime, requests
from bs4 import BeautifulSoup
from functools import wraps
from _process import loadMelonChart, loadArtistsChart, loggingData

def checkMelonChartSession():
	if "melonChart" not in session or "artistsChart" not in session:
		loggingData('Loading Session')
		
		session['melonChart'] = loadMelonChart()
		session['artistsChart'] = loadArtistsChart(session['melonChart'])

def getSongId(songName, melonChart):
	return [sublist for sublist in melonChart if songName in sublist][0][3]

def listNumbers(i: int):
	return f"{i + 1:03}"
	
def getSongArtistsSongs(melonChart, artistsName):
	return [sublist for sublist in melonChart if artistsName in sublist]

def getDayFlow(day):
	return str(datetime.date.today() - datetime.date(int(day.split(".")[0]), int(day.split(".")[1]), int(day.split(".")[2]))).split()[0]
	

class GetFromMelon():
	def __init__(self, songId, melonChart):
		self.songId = songId
		self.melonChart = melonChart
	
	def getSongNamed(self):
		return [sublist for sublist in self.melonChart if self.songId in sublist][0][1]
	
	def getLimitSongName(self):
		return f'{"".join(GetFromMelon(self.songId, self.melonChart).getSongNamed()[:8])}...'

	def getSongArtists(self):
		return [sublist for sublist in self.melonChart if self.songId in sublist][0][2]
		
	def getSongLikes(self):
		return [sublist for sublist in self.melonChart if self.songId in sublist][0][5]

	def getIntegerSongLikes(self):
		return GetFromMelon(self.songId, self.melonChart).getSongLikes().replace(",", "")

	def getSongLyric(self):
		return scrapeMelon.getLyric(self.songId).replace('\n', '<br>')

	def getSongRelease(self):
		html = requests.get(f"https://www.melon.com/song/detail.htm?songId={self.songId}", headers={"User-Agent": "github.com/hanluca/Melonpy"}).text
        
		return BeautifulSoup(html, "lxml").find_all("dd", limit=2)[1].getText()

	def getSongAlbumImg(self):
		html = requests.get(f"https://www.melon.com/song/detail.htm?songId={self.songId}", headers={"User-Agent": "github.com/hanluca/Melonpy"}).text
        
		return BeautifulSoup(html, "lxml").find("img", {"onerror" : "WEBPOCIMG.defaultAlbumImg(this);"}).get("src")
