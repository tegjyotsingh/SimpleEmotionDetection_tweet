#Classify the Preprocessed tweets file into Positive or NEgative categories.
# Sample with 20 tweets file.
from pattern.vector import Document,Bayes,LSA, Corpus,PORTER,TFIDF
from numpy import diag,dot
from numpy.linalg import svd
filename='sample_20'
f=open(filename,'r')
lines=f.readlines()
Positive=lines[9:]
Negative=lines[:9]
Type=[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]
docs=[]
for text in lines:
	vec=Document(text,stopword=True,stemmer=PORTER,type='1')
	docs.append(vec)

corpus=Corpus(documents=docs,weight=TFIDF)
print corpus.vectors
corpus.reduce(3)
print "hi"
print corpus.lsa.vectors

f.close()
