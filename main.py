
from codechef import *
from os import mkdir

usr = Profile()
usr.get_user_handle()

ques_list = usr.get_solved_problems()

fld_name = "CodeChef-" + usr.handle
try:
	mkdir(fld_name)
except FileExistsError:
	pass

for ques in ques_list:
	sub_link = ques_list[ques]
	code_link = usr.get_AC_submission(sub_link)
	n_tpl = usr.extract_code(ques_list[ques])
	write_to_file(n_tpl[1], fld_name, ques, n_tpl[0])

