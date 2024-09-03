from melonapi import scrapeMelon
import json, datetime

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
	
	for i in range(0, 10):
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

def getSongId():
	SongIds = []

	for song in listedMelonChart():
		SongIds.append(song['songId'])

	return SongIds
	
def getSongLyric(SongID):
	MelonSongLyric = scrapeMelon.getLyric(SongID).replace('\n', '<br>')
	return MelonSongLyric

def getSongName(SongID, Mode = "limit"):
	SongNames = {}

	for song in listedMelonChart():
		SongName = list(song['name'])

		if Mode == 'limit':
			if len(SongName) > 8:
				SongNames[song['songId']] = f'{"".join(SongName[:8])}...'
		
			else:
				SongNames[song['songId']] = song['name']

		else:
			SongNames[song['songId']] = song['name']

	return SongNames[SongID]

def listNumbers(i: int):
	return f"{i + 1:03}"

def getDayFlow(day):
	day = day.split(".")
	return datetime.date.today() - datetime.date(int(day[0]), int(day[1]), int(day[2]))