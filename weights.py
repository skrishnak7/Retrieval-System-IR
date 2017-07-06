from __future__ import division
import math
import re
import sys
from collections import Counter
import operator
from docstats import getWordTF,getmaxtf,getdocFreq
#from sample import documents
#docslen=getdoclens(documents)
#avgdoclen=sum(doclens)/len(doclens)

def weight1(term,document,documents):
     tf= getWordTF(term,document)
     maxtf = getmaxtf(document)
     if term in document:
     	w1= (0.4+0.6*math.log(tf+0.5)/math.log(maxtf+1.0))
     else:
        w1=0	
     return w1  

def weight11(term,document,documents):
     tf= getWordTF(term,document)
     maxtf = getmaxtf(document)
     cs=1400
     df=getdocFreq(term,documents)
     if term in document:
     	w1= (0.4+0.6*math.log(  tf+0.5)/math.log(maxtf+1.0))*(math.log(cs/df)/math.log(cs))  
     else:
        w1=0

     return w1

def weight2(term,document,documents):
	tf=getWordTF(term,document)
	doclen=len(document)
	avgdoclen=104
	w2=(0.4 + 0.6*(tf/(tf+0.5+1.5*(doclen/avgdoclen))))
	return w2


def weight21(term,document,documents):
	tf=getWordTF(term,document)
	doclen=len(document)
	df=getdocFreq(term,documents)
	avgdoclen=104
	cs=1400
	if(df != 0):
		w2=(0.4 + 0.6*(tf/(tf+0.5+1.5*(doclen/avgdoclen))))*(math.log(cs/df)/math.log(cs))
	else:
		w2=0

	return w2 	

def documentVector(doc,documents):
	vector=[]
	for term in doc:
		dummy=[]
		w1td = weight11(term,doc,documents)
		w1td = w1td/math.sqrt(len(doc))
		dummy.append(term)
		dummy.append(w1td)
		if w1td != 0:
			vector.append(dummy)
	return vector	

def queryVector(query,documents):
	vector=[]
	for term in query:
		dummy=[]
		w1tq= weight2(term,query,documents)
		w1tq= w1tq/math.sqrt(len(query))
		dummy.append(term)
		dummy.append(w1tq)
		if w1tq != 0:
			vector.append(dummy)

	return vector		

def cosineScore(query,documents):
    
	scores=[]
	lq=len(query)
	scoredoc1= range(len(documents))
	
	for term in query:
		w1tq=weight1(term,query,documents)
		score=0
		docid=0
		for doc in documents:
			w1td=weight11(term,doc,documents) 	
			score = w1td*w1tq
			scoredoc1[docid] = score
			docid+=1
	
	docid=0		
	for doc in documents:
		dummy=[]
		ld=len(doc)
		scoredoc1[docid]=scoredoc1[docid]/(math.sqrt(ld)*math.sqrt(lq))
		dummy.append(docid)
		dummy.append(scoredoc1[docid])
		scores.append(dummy)
		docid+=1
	
	scores = (sorted(scores,key=operator.itemgetter(1),reverse= True))	

	return scores		 

def cosineScore2(query,documents):
    
	scores=[]
	lq=len(query)
	scoredoc1= range(len(documents))
	
	for term in query:
		w1tq=weight2(term,query,documents)
		score=0
		docid=0
		for doc in documents:
			w1td=weight21(term,doc,documents) 	
			score = w1td*w1tq
			scoredoc1[docid] = score
			docid+=1
	
	docid=0		
	for doc in documents:
		dummy=[]
		ld=len(doc)
		scoredoc1[docid]=scoredoc1[docid]/(math.sqrt(ld)*math.sqrt(lq))
		dummy.append(docid)
		dummy.append(scoredoc1[docid])
		scores.append(dummy)
		docid+=1
	
	scores = (sorted(scores,key=operator.itemgetter(1),reverse= True))	

	return scores		 


doc = "the two-dimensional steady boundary-layer problem for a flat plate in a shear flow of incompressible fluid is considered .solutions for the boundarylayer thickness, skin friction, and the velocity distribution in the boundary layer are obtained by the karman-pohlhausen technique. comparison with the boundary layer of a uniform flow has also been made to show the effect of vorticity."
term = "boundary"

document = doc.split()

p=[1,2,3,4,5,6,7,8,9,1]
p1=p[:5]

#print p1
#print weight1(term,document)
#print weight2(term,document)

#f= open('./cranfield0001','r')
#str1=""
#for line in f:
#	str1+=line
	
#title= re.compile('<TITLE *[^>]*>.*</TITLE*>',re.DOTALL).findall(str1)

#str1  = re.sub('<.*?>', '', str1)
#str1  = re.sub(r'[^\sa-zA-Z]', '', str1)

#title1 = re.sub('<.*?>', '', title[0])
#title1 = re.sub(r'[^\sa-zA-Z]', '', title1)

#print str1
#print title1

#print type(title)
#print type(str1)