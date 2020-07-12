from pymongo import MongoClient
from pprint import pprint
import os.path
import datetime
import time
from os import path
import first
import third

def main():
	client=MongoClient("mongodb://localhost")
	db=client.admin
	fp_of_log=open("access.log","r")
	while True:
		first.handler(fp_of_log)
		print("Delete Access File work", datetime.datetime.now())
		#os.remove("temp.log")
		print("copy_access file sucessfully deleted")
		time.sleep(2)
		third.List_Out_Directory(db)

if __name__=="__main__":
	main()
