from flask import Blueprint, session, url_for, render_template, redirect

#from _functions import listedMelonChart, listNumbers, getSongLyric, listedArtists, getStatistics, getArtistSong, getSongName, getSongId, getDayFlow, checkMelonChartSession
from _functions import checkMelonChartSession, listNumbers, GetFromMelon
from _addon import MelonAddon

music_page = Blueprint('musicPage', __name__, template_folder='templates/music_page')


@music_page.route('/top100')
def musicPage__Top100():
	checkMelonChartSession()
	
	return render_template(
		'music_page__top100.html',
		title='Melonpy : Top100',
		listedMelonChart=session['melonChart'],
		listNumbers=listNumbers
	)
	
@music_page.route('/statistics/<songid>')
def musicPage__Statistics(songid):
	checkMelonChartSession()

	melonChart = session['melonChart']

	return render_template(
		'music_page__statistics.html',
		title=f'Melonpy : Statistics  :: {GetFromMelon(songid, melonChart).getSongNamed()}',
		songName = GetFromMelon(songid, melonChart).getSongNamed(),
		songLikes = GetFromMelon(songid, melonChart).getSongLikes(),
		songLikesInt = GetFromMelon(songid, melonChart).getIntegerSongLikes(),
		songRelease = GetFromMelon(songid, melonChart).getSongRelease()
	)

@music_page.route('/lyric/<songid>')
def musicPage__Lyric(songid):
	checkMelonChartSession()
	
	melonChart = session['melonChart']
	Lyric = GetFromMelon(songid, melonChart).getSongLyric()
	
	return render_template(
		'music_page__lyric.html',
		title='Melonpy : Lyric',
		Lyric=Lyric,
		songid=songid,
		#SongName=getSongName(songid),
		#SongTitle=getSongName(songid, 'None')
	)

@music_page.route('/artistsrank')
def musicPage__ArtistsRank():
	return render_template(
		'music_page__artistsrank.html',
		title='Melonpy : Artists Ranking',
		#Statistics=getStatistics(),
		#listNumbers=listNumbers,
		iconList=[
			'<span class="material-symbols-outlined">social_leaderboard</span>', # 1
			'<span class="material-symbols-outlined">workspace_premium</span>', # 2
			'<span class="material-symbols-outlined">license</span>', # 3	
		]
	)

@music_page.route('/artists/<name>')
def musicPage__Artists(name):
	return render_template(
		'music_page__artists.html',
		title='Melonpy : Songs',
		#ArtistsSongs=getArtistSong(name)
	)