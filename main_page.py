from flask import Blueprint, url_for, render_template, redirect, session
import json

#from _functions import listedMelonChart, listNumbers, getSongName
from _process import loadMelonChart

main_page = Blueprint('mainPage', __name__, template_folder='templates/main_page')

@main_page.route('/')
def mainPage__Emthy():
	return redirect(url_for('mainPage.mainPage__Home'))

@main_page.route('/home')
def mainPage__Home():
	if 'melonChart' in session: pass
	else:
		session['melonChart'] = loadMelonChart()
	
	return render_template(
		'main_page__home.html',
		title='Melonpy'
	)

@main_page.route('/about')
def mainPage__About():
	return render_template(
		'main_page__about.html',
		title='Melonpy : About'
	)