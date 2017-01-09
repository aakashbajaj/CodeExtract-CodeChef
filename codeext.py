from bs4 import BeautifulSoup
import urllib.request
import userhandle

try:
	from urllib.request import urlopen
	# For Python 3.0 and later
except ImportError:
	import urllib2
	# For Python 2's

get_user_handle()

with open('username.txt','r') as uname:
	user_name = str(uname.read().strip())
		