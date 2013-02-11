import urllib, httplib2, os, sys, csv, time
from httplib import BadStatusLine
try:
	import json
except ImportError:
	import simplejson as json

#SETTINGS#
gilt_api_key = ''

def GiltUpcomingSales(gilt_store, gilt_api_key):
	if gilt_store != '':
		url = '/sales/' + gilt_store + '/upcoming.json?apikey=' + gilt_api_key
	else:
		url = '/sales/upcoming.json&apikey=' + gilt_api_key
	headers = {}
	body = ""
	response, content = http.request(gilt_url_base+url, 'GET', headers=headers, body=body)
	return content

def GiltSaleDetail(gilt_store, gilt_sale_key, gilt_api_key):
	if gilt_store == '':
		return "Please specify a Store."
	elif gilt_sale_key == '':
		return "Please specify a Sale ID."
	else:
		url = '/sales/' + gilt_store + '/' + sale_key + 'detail.json?apikey=' + gilt_api_key
	headers = {}
	body = ""
	response, content = http.request(gilt_url_base+url, 'GET', headers=headers, body=body)
	return content
	
def GiltProductDetail(gilt_product_id, gilt_api_key):
	if gilt_product_id == '':
		return "Please specify a Product ID"
	else:
		url = '/products/' + gilt_product_id + '/detail.json?apikey=' + gilt_api_key
	headers = {}
	body = ""
	response, content = http.request(gilt_url_base+url, 'GET', headers=headers, body=body)
	return content
	
def GiltProductCategories(gilt_api_key):
	url = '/products/categories.json?apikey=' + gilt_api_key
	headers = {}
	body = ""
	response, content = http.request(gilt_url_base+url, 'GET', headers=headers, body=body)
	return content

def GiltActiveSales(gilt_store, gilt_api_key):
	if gilt_store == '':
		url = '/sales/active.json&apikey=' + gilt_api_key
	else:
		url = '/sales/' + gilt_store + '/active.json?apikey=' + gilt_api_key
	headers = {}
	body = ""
	response, content = http.request(gilt_url_base+url, 'GET', headers=headers, body=body)
	return content

#GiltSalesSearch uses JOSQL for the search term. See https://betadev.gilt.com/documentation/resources.html#josql_syntax for more information.
# TO DO: clean up search terms for passing as URL parameter
def GiltSalesSearch(gilt_search_term, gilt_api_key):
	if gilt_search_term == '':
		return "Please specify a search term."
	else:
		url = '/sales/josql?apikey=' + gilt_api_key + "&q=" + gilt_search_term
	headers = {}
	body = ""
	response, content = http.request(gilt_url_base+url, 'GET', headers=headers, body=body)
	return content

#You'll have to specify which store to connect to before using many of these functions. Options are:
# 'women' for the Women's store
# 'men' for the Men's store
# 'kids' for the Baby & Kids store
# 'home' for the Home store

gilt_store = ''
