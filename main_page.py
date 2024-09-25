from flask import Blueprint, url_for, render_template, redirect, session, after_this_request
import json, threading

#from _functions import listedMelonChart, listNumbers, getSongName
from _process import loadArtistsChart
from _functions import checkMelonChartSession

main_page = Blueprint('mainPage', __name__, template_folder='templates/main_page')

@main_page.route('/')
def mainPage__Emthy():	
	return redirect(url_for('mainPage.mainPage__Home'))

@main_page.route('/home')
def mainPage__Home():
	return render_template(
		'main_page__home.html',
		title='Melonpy',
		mainPage=True
	)

@main_page.route('/about')
def mainPage__About():
	return render_template(
		'main_page__about.html',
		title='Melonpy : About',
		backMode="musicPage.musicPage__Top100",
		usedModulFile = open("requirements.txt", "r").read().replace("\n", "<br>")
	)

@main_page.route('/setting/<setting>')
def mainPage__Setting(setting):
	if setting == 'sessionReset':
		session.clear()
		return redirect(url_for('mainPage.mainPage__Home'))
	
	return render_template(
		'main_page__setting.html',
		title='Melonpy : Setting',
		backMode="mainPage.mainPage__Home",
	)