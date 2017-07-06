from __future__ import division
import re
import sys
import os
from nltk.stem import WordNetLemmatizer
import operator
import nltk
from collections import Counter
import pickle 
import math
from weights import weight1,weight2,weight21,weight11,cosineScore,cosineScore2,queryVector,documentVector
from docstats import getStopWords,getWordTF,getdocFreq,getdoclens,getmaxtf

def gettag(j):
	if j in {'VB','VBD','VBG','VBN','VBP','VBP','VBZ'}:
		return 'v'
	elif j in {'RB','RBR','RBS'}:
		return 'r'
	elif j in {'JJ','JJR','JJS'}:
		return 'a'
	elif j in {'NN','NNS','NNP','NNPS'}:
		return 'n'				
	else:
		return 'n'

stopwords = getStopWords('stopwords')  

l1 = WordNetLemmatizer()
total_words =[]
path = "./Cranfield/"
#path =".\Test\\"
path_query = "./Query/"

dirs = os.listdir(path)
dirs_query = os.listdir(path_query)

documents=[] ## stores all the documents 
queries=[] ##scores the queries
doc_title=[] #store the titles of the documents

for filename in dirs :
	txt = open (path + filename , 'r')
	str1= ""
	raw_doc=[]
	for line in txt:
		#line  = re.sub('<.*?>', '', line)
		#line  = re.sub(r'[^\sa-zA-Z]', '', line)
		str1 += line

	#Retrieving the title of the document
	title= re.compile('<TITLE *[^>]*>.*</TITLE*>',re.DOTALL).findall(str1)
	title1 = re.sub('<.*?>', '', title[0])
	title1 = re.sub(r'[^\sa-zA-Z]', '', title1)
	str1  = re.sub('<.*?>', '', str1)
	str1  = re.sub(r'[^\sa-zA-Z]', '', str1)
	text = str1.split()	
	text = [i.lower() for i in text ]
	rec=nltk.pos_tag(text)
	for i,j in rec:
		if (i in stopwords):
			#raw_doc.append(i)
			continue
		else:
			l=gettag(j)
			l2=l1.lemmatize(i,pos=l)
			raw_doc.append(l2)
			total_words.append(l2)
		
	documents.append(raw_doc)
	doc_title.append(title1)
      
z1=Counter(total_words)

#for loop for getting the queries from 
for query in dirs_query :
	q = open(path_query+query,'r')
	qstr1=""
	raw_query=[]
	for line in q:
		line  = re.sub(r'[^\sa-zA-Z]', '', line)
		qstr1+=line

	qtext = qstr1.split()
	qtext = [i.lower() for i in qtext]
	tag= nltk.pos_tag(qtext)
	
	for i,j in tag:
		if (i in stopwords):
			continue
		else:
			l=gettag(j)
			l2=l1.lemmatize(i,pos=l)
			raw_query.append(l2)

	queries.append(raw_query)		


docslen = getdoclens(documents)
avgdoclen = sum(docslen)/len(docslen)

#for query in queries:
    #print query
#    p=cosineScore(query,documents)
#    print queryVector(query,documents)
#    print p[:10] 
#print "############################"
#for doc in documents:
#	print documentVector(doc,documents)
#print queries[0]
#p = cosineScore(queries[19],documents)
#print queryVector(queries[0],documents)
#print documentVector(documents[0],documents)    

#print len(p)
#print p[:10] 					 

#x = (sorted(p,key=operator.itemgetter(1),reverse= True))
#print x

nf= open("querycosines","w+")
qcount=1
for query in queries:
    print "Weighting Scheme1"
    print qcount,"##################"
    p=cosineScore(query,documents)
    p1=p[:5]
    print p1
    print>>nf,qcount,query
    print qcount,query
    for i ,j in p1:
    	count=1
    	x=doc_title[i]
    	print count,j,i,x
    	print>>nf,count,j,i,x
    	count+=1
    qcount+=1	


qcount=1
    	
for query in queries:
	print "W Scheme2"
	print qcount,"##############"
	p=cosineScore2(query,documents)
	p1=p[:5]
	print p1
	count=1
	for i,j in p1:
		x=doc_title[i]
		print count,j,i,x
		count = count +1
    #qcount+=1

nf.close()	