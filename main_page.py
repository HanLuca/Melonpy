from flask import Blueprint, url_for, render_template, redirect

from _functions import listedMelonChart, listNumbers

main_page = Blueprint('mainPage', __name__, template_folder='templates/main_page')

@main_page.route('/')
def mainPage__Emthy():
	return redirect(url_for('mainPage.mainPage__Home'))

@main_page.route('/home')
def mainPage__Home():	
	return render_template(
		'main_page__home.html',
		title='dd'
	)