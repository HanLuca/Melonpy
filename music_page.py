from flask import Blueprint, url_for, render_template, redirect

from _functions import listedMelonChart, listNumbers, getSongLyric, listedArtists, getStatistics, getArtistSong, getSongName, getSongId, getDayFlow
from _addon import MelonAddon

music_page = Blueprint('musicPage', __name__, template_folder='templates/music_page')

@music_page.route('/top100')
def musicPage__Top100():
	return render_template(
		'music_page__top100.html',
		title='Melonpy : Top100',
		listedMelonChart=listedMelonChart(),
		listNumbers=listNumbers
	)

@music_page.route('/statistics/<songid>')
def musicPage__Statistics(songid):
	songRelease = MelonAddon.getSongWhenRelease(songid)

	return render_template(
		'music_page__statistics.html',
		title='Melonpy : Statistics',
		songLikes=MelonAddon.getSongLikesList()[int(getSongId().index(songid))],
		songRelease=songRelease,
		comments=MelonAddon.getCommentAmount(songid),
		dayFlow = getDayFlow(songRelease)
	)

@music_page.route('/lyric/<songid>')
def musicPage__Lyric(songid):
	Lyric = getSongLyric(songid)
	
	return render_template(
		'music_page__lyric.html',
		title='Melonpy : Lyric',
		Lyric=Lyric,
		songid=songid,
		SongName=getSongName(songid),
		SongTitle=getSongName(songid, 'None')
	)

@music_page.route('/artistsrank')
def musicPage__ArtistsRank():
	return render_template(
		'music_page__artistsrank.html',
		title='Melonpy : Artists Ranking',
		Statistics=getStatistics(),
		listNumbers=listNumbers,
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
		ArtistsSongs=getArtistSong(name)
	)