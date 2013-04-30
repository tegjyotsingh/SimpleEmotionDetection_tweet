
#Demo file for getting tweets
from pattern.web import Twitter, plaintext
from pattern.en.wordlist import BASIC,ACADEMIC,PROFANITY,TIME



for tweet in Twitter().search('#anger', cached=False,language='en', sort ='RELEVANCY',count=100):
	t= plaintext(tweet.description)
	words=t.split(" ")
	words = [w for w in words if w in ACADEMIC or w  in BASIC or w  in PROFANITY or w in TIME ]
	print ' '.join(words)
	#print ACADEMIC
	#print t
	print '----'
