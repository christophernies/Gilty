import urllib, httplib2, os, sys, csv, time
from httplib import BadStatusLine
try:
	import json
except ImportError:
	import simplejson as json

def GiltUpcomingSales(store, gilt_api_key):
	if store != '':
		url = '/sales/' + store + '/upcoming.json?apikey=' + gilt_api_key
	else:
		url = '/sales/upcoming.json&apikey=' + gilt_api_key
	print url
	headers = {}
	body = ""
	response, content = http.request(gilt_url_base+url, 'GET', headers=headers, body=body)
	return content

def GiltSaleDetail(store, sale_key, gilt_api_key):
	if store != '':
		url = '/sales/' + store + '/' + sale_key + 'detail.json?apikey=' + gilt_api_key
	print url
	headers = {}
	body = ""
	response, content = http.request(gilt_url_base+url, 'GET', headers=headers, body=body)
	return content
	
def GiltProductDetail(product_id, gilt_api_key):
	if store != '':
		url = '/products/' + product_id + '/detail.json?apikey=' + gilt_api_key
	print url
	headers = {}
	body = ""
	response, content = http.request(gilt_url_base+url, 'GET', headers=headers, body=body)
	return content
	
def GiltProductDetail(gilt_api_key):
	if store != '':
		url = '/products/categories.json?apikey=' + gilt_api_key
	print url
	headers = {}
	body = ""
	response, content = http.request(gilt_url_base+url, 'GET', headers=headers, body=body)
	return content

def GiltActiveSales(store, gilt_api_key):
	if store != '':
		url = '/sales/' + store + '/active.json?apikey=' + gilt_api_key
	else:
		url = '/sales/active.json&apikey=' + gilt_api_key
	print url
	headers = {}
	body = ""
	response, content = http.request(gilt_url_base+url, 'GET', headers=headers, body=body)
	return content