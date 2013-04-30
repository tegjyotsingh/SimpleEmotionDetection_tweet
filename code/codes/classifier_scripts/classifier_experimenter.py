from pattern.vector import Document, Corpus, Bayes,WEKA,TFIDF,PORTER,IG


f_neg=open('Negative_pr','r')
f_pos=open('Positive_pr','r')
neg_lines=f_neg.readlines()
pos_lines=f_pos.readlines()

print 'Number of Positive Tweets:',len(pos_lines)
print 'Number of Negative Tweets:',len(neg_lines)

documents = []
for line in neg_lines:
    document = Document(line,stopword=False,stemmer=PORTER,type=0)
    documents.append(document)


for line in pos_lines:
    document = Document(line,stopword=False,stemmer=PORTER,type=1)
    documents.append(document)

corpus = Corpus(documents,weight=TFIDF)
print "number of documents:", len(corpus)
print "number of words:", len(corpus.vector)
print "number of words (average):", sum(len(d.terms) for d in corpus.documents) / float(len(corpus))
print



# Train Naive Bayes on all documents.
# To test the accuracy of a classifier, Using 10-fold crossvalidation
# This yields 4 scores: Accuracy, Precision, Recall and F-score.
print 'Bayes Classifier'
print  '-------------------------'
print  '(Accuracy, Precision,REcall,F-Measure)'
print Bayes.test(corpus,folds=10)


#Crossavalidation on reduced Dataset
nfeatures=10000
f=corpus.feature_selection(top=nfeatures,method=IG)
corpus=corpus.filter(features=f)
print 'Bayes Classifier on Reduced dataset of', nfeatures,' features'
print  '-------------------------'
print  '(Accuracy, Precision,REcall,F-Measure)'
print Bayes.test(corpus,folds=10)


#Testing Model on sample Dataset
print 'Testing Model on Sample Dataset'
classifier = Bayes()
for document in corpus.documents:
    classifier.train(document,type=document.type)
# In the file top 10 are negative tweets and rest are positive tweets
ft=open('test_20','r')
test_lines=ft.readlines()
for line in test_lines:
	t=(Document(line))
	corpus.append(t)
	print line.strip()+' '+str(classifier.classify(t))
ft.close()

#Export reduced Features file to Arff file
print 'Exporting Corpus to Weka format'
corpus.export('Weka_PAtterns.arff',format=WEKA)

f_neg.close()
f_pos.close()

