import os
import second
import datetime
import time


def Generate_Copy_File(fp_of_log):
	
	print("Run function work", datetime.datetime.now())
	print("File Copy start\n")
	fp_of_tlog = open("temp.log", "a")
	n = second.Copy_File(fp_of_tlog,fp_of_log)
	if n == "EOF":
		print("Waiting for some time to generate log file....!\n")
		time.sleep(2)
	print("File Copy complete \n")

def Run_Sarg(): 
	
	print("Run Sarg work", datetime.datetime.now())
	os.system('sarg -x')
	print("sarg Complete work")

def Delete_templog_File():

	print("Delete Access File work", datetime.datetime.now())
	os.remove("temp.log")
	print("copy_access file sucessfully deleted")
	time.sleep(2)


def handler(fp_of_log):

	#fp2 = open("access.log", "r")
	Generate_Copy_File(fp_of_log)
	Run_Sarg()
	#print("Delete file")
	time.sleep(2)
	Delete_templog_File()
	print("Acces file delete")
