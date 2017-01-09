from util import *
from bs4 import BeautifulSoup

class Profile(object):
	
	"""Profile Class For User"""

	def __init__(self, handle=""):
		super(Profile, self).__init__()
		self.handle = handle
		self.domain_url = "https://www.codechef.com/"


	def get_user_handle(self):
		self.usr_name = ''
		first_time = True
		while len(self.usr_name) == 0:
			if first_time:
				first_time = False
			else:
				print("You haven't entered any handle. Please try again.")

			self.usr_name = input("Enter Your CodeChef Handle: ").strip()


	def get_solved_problems(self):
		"""Function Processes the user page and return a dictionary object containing all successfully solved problems"""
		"""Return format { problem_code : problem_link }"""
		domain_url = self.domain_url
		handle = self.handle
		user_url = domain_url + "users/" + handle
		user_page = get_url_data(user_url)
		soup = BeautifulSoup(user_page)
		# Segregate problems table
		sp = soup.find_all('table')[2]
		
		prob_list = {}

		for cell in sp.find_all('td'):
			if cell.text == "Problems Successfully Solved:":
				n_soup = cell.nextSibling.nextSibling

		for s in n_soup.find_all('a'):
			prob_list[s.text.strip()] = (str(s.get('href'))).strip()

		return prob_list