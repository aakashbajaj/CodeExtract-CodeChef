
def get_user_handle():
	usr_name = ''
	first_time = True
	while len(usr_name) == 0:
		if first_time:
			first_time = False
		else:
			print("You haven't entered any handle. Please try again.")

		usr_name = input("Enter Your CodeChef Handle: ").strip()

	with open('username.txt','w') as fl:
		fl.write(usr_name)