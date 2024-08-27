from melonapi import scrapeMelon
import json

def findKeys(dict, val):
  return list(key for key, value in dict.items() if value == val)
	
def listedMelonChart():
	MelonChart = json.loads(scrapeMelon.getList('LIVE').decode()) # string -> dic
	ListedMelonChart = []

	for i in range(1, 101):
		ListedMelonChart.append(MelonChart[str(i)])

	return ListedMelonChart

def listedArtists():
	listedArtists = {}
	
	for song in listedMelonChart():	
		artists = str(song['artists'])
		
		if artists in listedArtists: listedArtists[artists] += 1
		else: listedArtists[artists] = 1

	return listedArtists

def getStatistics():
	Statistics = {}
	
	numberingArtists = sorted(listedArtists().values(), reverse=True)
	forList = []; indexList = []
	
	for i in range(0, 5):
		forList.append(findKeys(listedArtists(), numberingArtists[i]))
		indexList.append(numberingArtists[i])
	
	Statistics['mode'] = forList
	Statistics['modeIndex'] = indexList
	
	return Statistics

def getArtistSong(ArtistName):
	Artists = {}

	for song in listedMelonChart():
		Artists[song['name']] = song['artists']
	
	return findKeys(Artists, ArtistName)
	
def getSongLyric(SongID):
	MelonSongLyric = scrapeMelon.getLyric(SongID).replace('\n', '<br>')
	return MelonSongLyric

def listNumbers(i: int):
	return f"{i + 1:03}"