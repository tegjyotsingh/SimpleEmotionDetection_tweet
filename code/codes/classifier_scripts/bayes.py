#Running Naive Bayes on the Tweets DAta
from pattern.vector import Document, Corpus, Bayes,WEKA,TFIDF,PORTER,IG,TOP300,COSINE,KNN,SVM,LINEAR,CLASSIFICATION

#Import The Preprocessed Tweets
f_neg=open('Negative_pr','r')
f_pos=open('Positive_pr','r')
neg_lines=f_neg.readlines()
pos_lines=f_pos.readlines()
print 'Number of Negative Tweets:',len(neg_lines)
print 'Number of Positive Tweets:',len(pos_lines)

documents = []
for line in neg_lines:
    document = Document(line,stopword=True,stemmer=PORTER,type=0)
    documents.append(document)

for line in pos_lines:
    document = Document(line,stopword=True,stemmer=PORTER,type=1)
    documents.append(document)

corpus = Corpus(documents,weight=TFIDF)
print "number of documents:", len(corpus)
print "number of words:", len(corpus.vector)
print "number of words (average):", sum(len(d.terms) for d in corpus.documents) / float(len(corpus))
print

classifier=Bayes(aligned=True)
for document in corpus:
    classifier.train(document,type=document.type)
print 'Done training'

# To test the accuracy of a classifier, Using 10-fold crossvalidation
# This yields 4 scores: Accuracy, Precision, Recall and F-score.
print 'Bayes Classifier'
print  '-------------------------'
print  '(Accuracy, Precision,REcall,F-Measure)'
print Bayes.test(corpus.documents,folds=10)

#Testing on the Sample dataset of 10 Negative and 10 Positive Tweets
ft=open('test_20','r')
test_lines=ft.readlines()
for line in test_lines:
	t=(Document(line))
	corpus.append(t)
	print line.strip(),' ',str(classifier.classify(t))
ft.close()
f_neg.close()
f_pos.close()

