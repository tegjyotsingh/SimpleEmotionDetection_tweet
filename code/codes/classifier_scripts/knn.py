#this script perform the KNN classification on the data
from pattern.vector import Document, Corpus, Bayes,WEKA,TFIDF,PORTER,IG,TOP300,COSINE,KNN

#Import The Preprocessed Tweets
f_neg=open('Negative_pr','r')
f_pos=open('Positive_pr','r')
neg_lines=f_neg.readlines()
pos_lines=f_pos.readlines()
print 'Number of Negative Tweets:',len(neg_lines)
print 'Number of Positive Tweets:',len(pos_lines)

documents = []
for line in neg_lines:
    document = Document(line,stopword=True,stemmer=PORTER,type='0')
    documents.append(document)
for line in pos_lines:
    document = Document(line,stopword=True,stemmer=PORTER,type='1')
    documents.append(document)

corpus = Corpus(documents,weight=TFIDF)
print "number of documents:", len(corpus)
print "number of words:", len(corpus.vector)
print "number of words (average):", sum(len(d.terms) for d in corpus.documents) / float(len(corpus))
print

#Filtering top 1000 features using Information Gain Criterion
corpus=corpus.filter(features=(corpus.feature_selection(top=1000,method=IG)))

# To test the accuracy of a classifier, Using 10-fold crossvalidation
# This yields 4 scores: Accuracy, Precision, Recall and F-score.
print 'classifying using KNN'
print  '-------------------------'
print  '(Accuracy, Precision,REcall,F-Measure)'
print KNN.test(corpus,k=100,folds=10,distance=COSINE)

f_neg.close()
f_pos.close()

