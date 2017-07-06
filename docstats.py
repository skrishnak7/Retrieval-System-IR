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

def getStopWords(filename):
	stopwords = []
	fp= open(filename,'r')
	line = fp.readline()
	while line:
		word =line.strip()
		stopwords.append(word)
		line = fp.readline()

	fp.close()
	return stopwords 

def getWordTF(word,doc):
	count=0
	for i in doc:
		if i==word:
			count=count+1

	return count	
     
def getdocFreq(word,documents):
	count=0
	for doc in documents:
		if word in doc:
			count+=1
	return count

def getdoclens(documents):
	docslen=[]
	for doc in documents:
		doc_len = len(doc)
		docslen.append(doc_len)
	return docslen

def getmaxtf(doc):
	terms=[]
	z=[]
	maxtf=0
	for term in doc:
		terms.append(term)
	z=Counter(terms)
	sorted_key = reversed(sorted(z.items(),key = operator.itemgetter(1)))
	for i,j in sorted_key:
		maxtf=j
		break

	return maxtf
