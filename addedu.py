from pymongo import MongoClient
def main():
    client=MongoClient("mongodb://localhost")
    db=client.project
    fp=open('edu.txt','r')
    l=[]
    for line in fp:
        d={}
        d['site']=line.rstrip("\n")
        l.append(d)
    #print(l)
    db.edu.insert_many(l)
if __name__=="__main__":
    main()
