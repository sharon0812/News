from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles
from ..models import Sources


# Views
@main.route('/')
def index():
	'''
	view root page function that returns the index the page and its data
	'''
	health_sources = get_sources('health')
	business_sources = get_sources('business')
	technology_sources = get_sources('technology')
	science_sources = get_sources('science')
	general_sources = get_sources('general')
	entertainment_sources = get_sources('entertainment')
	sports_sources = get_sources('sports')
	title = "News"

	return render_template('index.html',title = title, general_sources = general_sources, science_sources = science_sources, business_sources = business_sources,technology_sources = technology_sources, health_sources = health_sources, entertainment_sources = entertainment_sources, sports_sources = sports_sources)

@main.route('/sources/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
	title = f'NH | {id}'

	return render_template('articles.html',title= title,articles = articles)  