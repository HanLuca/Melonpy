# SongDetailList = [Ranking, SongName, Artists, SongId, AlbumId, Likes]

from melonapi import scrapeMelon
from flask import Flask, request, render_template, redirect, session, url_for
import json, datetime
from functools import wraps
from _process import loadMelonChart

def checkMelonChartSession():
	if "melonChart" not in session: 
		session['melonChart'] = loadMelonChart()

def getSongId(songName, melonChart):
	return [sublist for sublist in melonChart if songName in sublist][0][3]

def listNumbers(i: int):
	return f"{i + 1:03}"

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

# def getStatistics():
# 	Statistics = {}
# 	beforeIndex = 0
	
# 	numberingArtists = sorted(listedArtists().values(), reverse=True)
# 	forList = []; indexList = []
	
# 	for i in range(0, 10):
# 		if beforeIndex != numberingArtists[i]:
# 			beforeIndex = numberingArtists[i]
# 			forList.append(findKeys(listedArtists(), numberingArtists[i]))
# 			indexList.append(numberingArtists[i])

# 		else: pass
	
# 	Statistics['mode'] = forList
# 	Statistics['modeIndex'] = indexList
	
# 	print(Statistics)
# 	return Statistics

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
	