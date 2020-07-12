from pymongo import MongoClient
import os.path
from os import path
import re
from bs4 import BeautifulSoup
import requests
import html2text


def findTypeOfUrl(url,db):
		try:
			url=url.rstrip('\"')
			print(url)
			words=url.split(":")
			if "http" in words and "443" in words:
				words[0]="https"
				words.pop()
				url='.'.join(words)
			print(url)
			r = requests.get(url, timeout=15)
			soup = BeautifulSoup(r.content, 'html.parser')
			"""if soup.status_code == 200:
				print("ok")
			else:
				if soup.status_code==301 or soup.status_code==302:
					print("Not premission")
					return 'o'
			"""
			data = soup.find_all('title') + soup.find_all('meta') + soup.find_all('p') + soup.find_all('h1')
			result = []
			for p in data:
				result.append(p.get_text())
			result=[e for e in result if e!='']
			str_to_search=' '.join(result)

			print(str_to_search)

			j=db.joy.find({"$text":{"$search":str_to_search}},{"_id":0})
			e=db.edu.find({"$text":{"$search":str_to_search}},{"_id":0})
			c=db.shop.find({"$text":{"$search":str_to_search}},{"_id":0})
			m=db.med.find({"$text":{"$search":str_to_search}},{"_id":0})
			a=db.mat.find({"$text":{"$search":str_to_search}},{"_id":0})
			if j.count()>0 or e.count()>0 or c.count()>0 or a.count()>0 or m.count()>0:
				if j.count()>=e.count() and j.count()>=c.count() and j.count()>=m.count() and j.count()>=a.count():
					for i in range(0,j.count()):
						print(j[i])
					return 'j'
				elif e.count()>=j.count() and e.count()>=c.count() and e.count()>=m.count() and e.count()>=a.count():
					for i in range(0,e.count()):
						print(e[i])
					return 'e'
				elif c.count()>=j.count() and c.count()>=e.count() and c.count()>=m.count() and c.count()>=a.count():
					for i in range(0,c.count()):
						print(c[i])
					return 'c'
				elif m.count()>=j.count() and m.count()>=e.count() and m.count()>=c.count() and m.count()>=a.count():
					for i in range(0,m.count()):
						print(m[i])
					return 'm'
				elif a.count()>=j.count() and a.count()>=e.count() and a.count()>=c.count() and m.count()>=a.count():
					for i in range(0,a.count()):
						print(a[i])
					return 'a'
				else:
					return 'o'
			else:
				return 'o'
		except Exception as E:
			print(E)
			return 'o'	
def findMax(turl,db,j,e,c,m,a):
		if j.count()>0 or e.count()>0 or c.count()>0 or a.count()>0 or m.count()>0:
			if j.count()>=e.count() and j.count()>=c.count() and j.count()>=m.count() and j.count()>=a.count():
				for i in range(0,j.count()):
					print(j[i])
				return 'j'
			elif e.count()>=j.count() and e.count()>=c.count() and e.count()>=m.count() and e.count()>=a.count():
				for i in range(0,e.count()):
					print(e[i])
				return 'e'
			elif c.count()>=j.count() and c.count()>=e.count() and c.count()>=m.count() and c.count()>=a.count():
				for i in range(0,c.count()):
					print(c[i])
				return 'c'
			elif m.count()>=j.count() and m.count()>=e.count() and m.count()>=c.count() and m.count()>=a.count():
				for i in range(0,m.count()):
					print(m[i])
				return 'm'
			elif a.count()>=j.count() and a.count()>=e.count() and a.count()>=c.count() and m.count()>=a.count():
				for i in range(0,a.count()):
					print(a[i])
				return 'a'
			else:
				return findTypeOfUrl(turl,db)
		else:
			return findTypeOfUrl(turl,db)
def Check_User_Indb(username,db):
	x=db.users.find({"_id":username})
	if x.count()>0:
		return 1
	else: return 0

def Check_Url_Indb(turl,url,db):
        
        #print("turl = ",turl)
        #print("url = ", url)
        list_of_words=url.split(".")
        list_of_words.pop()
		#dq='\"'
        str_to_search=''
        for i in list_of_words:
            str_to_search=str_to_search+" "+i
	#str_to_search="\""+str_to_search.lstrip()+"\""#
	#print(str_to_search)
	#x=db.sites.find({"$text":{"$search":str_to_search}},{"_id":0})
        j=db.joy.find({"$text":{"$search":str_to_search}},{"_id":0})
        e=db.edu.find({"$text":{"$search":str_to_search}},{"_id":0})
        c=db.shop.find({"$text":{"$search":str_to_search}},{"_id":0})
        m=db.med.find({"$text":{"$search":str_to_search}},{"_id":0})
        a=db.mat.find({"$text":{"$search":str_to_search}},{"_id":0})
        #print(j)
        value=findMax(turl,db,j,e,c,m,a)
        return value

def Open_And_Read_File(FilePath, HtmlFile,db):

		#OutputFile = open("OutputFile1", "a")
	path = FilePath +"/"+ HtmlFile
	username=FilePath.split("/")[1].rstrip()
	data = open(path, 'r')
	for line in data:
		if line.find("<tr>") != -1:
			index = line.rfind("<a href=")
			if index != -1:
				index=index+9
				turl=""
				while line[index]!=">":
					turl=turl+line[index]
					index+=1
				#print(turl)
				index+=1
				url=""
				while(line[index] != "<"):
					#OutputFile.write(line[index])
					url=url+line[index]
					index += 1
				linesplit=line.split("/td>")
				size=linesplit[3]
				index=size.find(">")
				index+=1
				bytestr=''
				while(True):
					if(size[index]=="M"):
						byte=float(bytestr)
						byte=byte*1024*1024
						break
					elif(size[index]=="K"):
						byte=float(bytestr)
						byte=byte*1024
						break
					elif(size[index]=="G"):
						byte=float(bytestr)
						byte=byte*1024*1024*1024
						break
					elif size[index]=="<":
						byte=float(bytestr)
						break
					else:
						bytestr=bytestr+size[index]
						index+=1
				response=Check_Url_Indb(turl,url,db)
				upf=Check_User_Indb(username,db)
				if upf==0:
					l={"_id":str(username),"j":0.0,"e":0.0,"c":0.0,"m":0.0,"a":0.0,"o":0.0,"total":0.0}
					l[str(response)]=byte
					l["total"]=byte
					db.users.insert_one(l)
				else:
					db.users.update_one({"_id":str(username)},{"$inc":{str(response):byte,"total":byte}})	
				#if upf==0:
def List_Out_Directory(db):
	d_list = list()
	all_subdirs = [d for d in os.listdir('.') if os.path.isdir(d)]
	DirectoryPath = max(all_subdirs, key=os.path.getmtime)
	files = os.listdir(DirectoryPath)

	for directory in files: 
		if os.path.isfile(DirectoryPath +"/"+ directory) != True:
			d_list.append(DirectoryPath +"/"+ directory)
	for users in d_list:
		UserHtmlFile = (users.split('/'))[1]
		files = os.listdir(users)
		for htmlFile in files:
			htmlFiles = UserHtmlFile + ".html"
			if htmlFile == htmlFiles:
				Open_And_Read_File(users, htmlFiles,db)
                                #print(users, htmlFiles)
if __name__=="__main__":
	client=MongoClient("mongodb://localhost")
	db=client.project
	List_Out_Directory(db)
