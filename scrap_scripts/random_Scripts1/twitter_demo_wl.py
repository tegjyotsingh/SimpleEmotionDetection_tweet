
#Demo file for getting tweets witrh updated wordlist
from pattern.web import Twitter, plaintext
from pattern.en.wordlist import BASIC,ACADEMIC,PROFANITY,TIME
from processTweet import processTweet,getotherhashtags
f=open('wordlist','r')
wl=f.read()
Wordlist=wl.split('\n')
for tweet in Twitter().search('#afraid', cached=False,language='en', sort ='RELEVANCY'):
	t=plaintext(tweet.description)
	
	#words = [w for w in words if w in ACADEMIC or w  in BASIC or w  in PROFANITY or w in TIME ]
	#print ' '.join(words)
	print t
	pt=processTweet(t)
	words=pt.split(" ")
	print pt
	
	words = [w for w in words if w in Wordlist ]
	
	print ' '.join(words)
	print getotherhashtags(t)
	
