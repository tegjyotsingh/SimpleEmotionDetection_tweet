#Classify the Preprocessed tweets file into Positive or NEgative categories.
# Sample with 20 tweets file.
from pattern.vector import Document,Bayes,WEKA,NORM, Corpus,PORTER,TFIDF
filename='sample_20'
f=open(filename,'r')
lines=f.readlines()
Positive=lines[9:]
Negative=lines[:9]
Type=[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]
docs=[]
b=Bayes()
for text in Positive:
	vec=Document(text,stopword=True,stemmer=PORTER,type='3')
	docs.append(vec)
	#print d.vector
	#corpus.append(d)
	#print d.vector
	b.train(vec)
for text in Negative:
	vec=Document(text,stopword=True,stemmer=PORTER,type='2')
	docs.append(vec)
	#print d.vector
	#corpus.append(d)
	#print d.vector
	b.train(vec)



print b.classes
print b.classify('on my finance')
print b.test(docs,folds=5)
corpus=Corpus(documents=docs,weight=TFIDF)
b.train(corpus.documents)
print b.classes
print b.classify('on my finance')
print b.test(docs,folds=5)
print corpus.vectors

f.close()
