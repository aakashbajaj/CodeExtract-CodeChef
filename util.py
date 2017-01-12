from urllib.request import urlopen
import urllib.request

def get_url_data(url1):
	req = urllib.request.Request(url1, headers={'User-Agent': 'Mozilla/5.0'})
	html_pg = urllib.request.urlopen(req)
	return html_pg