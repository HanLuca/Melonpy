from flask import Blueprint, url_for, render_template, redirect

from _functions import listedMelonChart, listNumbers, getSongLyric, listedArtists, getStatistics, getArtistSong

music_page = Blueprint('musicPage', __name__, template_folder='templates/music_page')

@music_page.route('/lyric/<songid>')
def musicPage__Lyric(songid):
	Lyric = getSongLyric(songid)
	
	return render_template(
		'music_page__lyric.html',
		Lyric=Lyric
	)

@music_page.route('/artistsrank')
def musicPage__ArtistsRank():
	return render_template(
		'music_page__artistsrank.html',
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
		ArtistsSongs=getArtistSong(name)
	)