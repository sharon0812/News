 
import urllib.request,json
from .models import Sources,Articles
from datetime import datetime
import os


#getting the api key
api_key = None

#getting the news base url
base_url = None

#getting the articles url
articles_url = None

def configure_request(app):

	global api_key,base_url,articles_url
	api_key = app.config['API_KEY'] 
	print (api_key)
	base_url = app.config['NEWS_SOURCES_BASE_URL']
	print(base_url)
	articles_url = app.config['ARTICLES_BASE_URL']

def get_sources(category):
	'''
	Function that gets the json response to our url request
	'''
	get_sources_url = base_url.format(api_key)

	with urllib.request.urlopen(get_sources_url) as url:
		get_sources_data = url.read()
		get_sources_response = json.loads(get_sources_data)
		print(get_sources_url)

		sources_results = None

		if get_sources_response['sources']:
			sources_results_list = get_sources_response['sources']
			sources_results = process_sources(sources_results_list)

	return sources_results 

def process_sources(sources_list):
	'''
	Function that processes the news sources results and turns them into a list of objects
	Args:
		sources_list: A list of dictionaries that contain sources details
	Returns:
		sources_results: A list of sources objects
	'''

	sources_results = []

	for source_item in sources_list:
		id = source_item['id'] 
		name = source_item['name']
		description = source_item['description']
		url = source_item['url']
		category = source_item['category']
		language = source_item['language']
		country = source_item['country']


		sources_object = Sources(id,name,description,url,category,country,language)
		sources_results.append(sources_object)


	return sources_results

def get_articles(id):
  '''
	Function that processes the articles and returns a list of articles objects
	'''
		
  get_articles_url = articles_url.format(id,api_key)

  with urllib.request.urlopen(get_articles_url) as url:
			articles_results = json.loads(url.read())

			articles_object = None
			if articles_results['articles']:
				articles_object = process_articles(articles_results['articles'])

			return articles_object

def process_articles(articles_list):
  
	articles_object = []
	for article_item in articles_list:
		# id = article_item['id']
		author = article_item['author']
		title = article_item['title']
		description = article_item['description']
		url = article_item['url']
		image = article_item['urlToImage']
		date = article_item['publishedAt']
		
		if image:
			articles_result = Articles(id,author,title,description,url,image,date)
			articles_object.append(articles_result)	

	return articles_object
