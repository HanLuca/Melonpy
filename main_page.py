from flask import Blueprint, url_for, render_template, redirect
import json

from _functions import listedMelonChart, listNumbers, getSongName

main_page = Blueprint('mainPage', __name__, template_folder='templates/main_page')

@main_page.route('/')
def mainPage__Emthy():
	return redirect(url_for('mainPage.mainPage__Home'))

@main_page.route('/home')
def mainPage__Home():
	return render_template(
		'main_page__home.html',
		title='Melonpy'
	)

@main_page.route('/about')
def mainPage__About():
	return render_template(
		'main_page__about.html',
		title='Melonpt : About'
	)