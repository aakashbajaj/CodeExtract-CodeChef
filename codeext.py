from bs4 import BeautifulSoup

try:
	from urllib.request import urlopen
	# For Python 3.0 and later
except ImportError:
	import urllib2
	# For Python 2's

# For The Final Code Page, Use the following request
# import urllib.request
# req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# html_pg = urllib.request.urlopen(req).read()

usr_flg = True

while usr_flg:
	try:
		with open('username.txt','r') as uname:
			user_name = str(uname.read().strip())
			usr_flg = False
	except FileNotFoundError:
		print("Can't Open File!")
		usr_flg = True