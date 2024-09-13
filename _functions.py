# SongDetailList = [Ranking, SongName, Artists, SongId, AlbumId, Likes]

from melonapi import scrapeMelon
from flask import Flask, request, render_template, redirect, session, url_for
import json, datetime, requests
from bs4 import BeautifulSoup
from functools import wraps
from _process import loadMelonChart, loadArtistsChart

def checkMelonChartSession():
	if "melonChart" not in session or "artistsChart" not in session:
		session['melonChart'] = loadMelonChart()
		session['artistsChart'] = loadArtistsChart(session['melonChart'])

def getSongId(songName, melonChart):
	return [sublist for sublist in melonChart if songName in sublist][0][3]

def listNumbers(i: int):
	return f"{i + 1:03}"
	
def getSongArtistsSongs(melonChart, artistsName):
	return [sublist for sublist in melonChart if artistsName in sublist]

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
		
	# 가사, 아티스트 랭크









# def findKeys(dict, val):
#   return list(key for key, value in dict.items() if value == val)
	
# def listedMelonChart():
# 	MelonChart = json.loads(scrapeMelon.getList('LIVE').decode()) # string -> dic
# 	ListedMelonChart = []

# 	for i in range(1, 101):
# 		ListedMelonChart.append(MelonChart[str(i)])

# 	return ListedMelonChart

# def listedArtists():
# 	listedArtists = {}
	
# 	for song in listedMelonChart():	
# 		artists = str(song['artists'])
		
# 		if artists in listedArtists: listedArtists[artists] += 1
# 		else: listedArtists[artists] = 1

# 	return listedArtists

# def getArtistSong(ArtistName):
# 	Artists = {}

# 	for song in listedMelonChart():
# 		Artists[song['name']] = song['artists']
	
# 	return findKeys(Artists, ArtistName)

# def getSongId():
# 	SongIds = []

# 	for song in listedMelonChart():
# 		SongIds.append(song['songId'])

# 	return SongIds
	
# def getSongLyric(SongID):
# 	MelonSongLyric = 
# 	return MelonSongLyric

# def getSongName(SongID, Mode = "limit"):
# 	SongNames = {}

# 	for song in listedMelonChart():
# 		SongName = list(song['name'])

# 		if Mode == 'limit':
# 			if len(SongName) > 8:
# 				SongNames[song['songId']] = f'{"".join(SongName[:8])}...'
		
# 			else:
# 				SongNames[song['songId']] = song['name']

# 		else:
# 			SongNames[song['songId']] = song['name']

# 	return SongNames[SongID]



# def getDayFlow(day):
# 	day = day.split(".")
# 	data = str(datetime.date.today() - datetime.date(int(day[0]), int(day[1]), int(day[2]))).split()[0]
# 	return data
	