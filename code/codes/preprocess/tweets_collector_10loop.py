#Script for collecting tweets from twitter based on a particulsr keyword.
#this script uses the Pattern Web Minng Library 

from pattern.web import Twitter,plaintext
#pattern.web contains methods for searching and collectng data from search engines,
#creating object for Twitter searchengine

#Generate_Tweets function generates tweets according to a particular search term and appends the tweets to a file given by the label which for this case is either : poistive or negative.


def Generate_Tweets(searchterm,filename_label):
	twitter_obj=Twitter(license=None, throttle=0.5,language='en')
	#throttle: time between requests.
	#now the twitter_obj can be searched, with the following parameters.
	
	# Twitter returns up to 1500 results for a search term. It has hourly limit of 150 queries. each call 	to search() is one query. So you can get like 15 queries of 100 each of 150 queries of 10 each.
	#  Parameters for Twitter: 
	#  Start 1-1500/count
	#  count: results per page=1-100
        #  SORT: RELEVANCY, Limit: 150/hour, throttle =0.5
	f=open(filename_label,'a')

	for tweet in twitter_obj.search(searchterm,cached=False,language='en', sort ='RELEVANCY',count=100):
		unicode_tweet=plaintext(tweet.description)
		#Tweets are unicode, need to be converted to ascii before storing in file
		ascii_tweet=unicode_tweet.encode('ascii','ignore')
		f.write(ascii_tweet+'\n')
	
	f.close()

def positive_tweets_collector(datafolder):
	searchterms_positive=['#joy','#happy','#bliss','#ecstatic','#merry']
	search_label='Positive'
	#Repeating tweet collection to get more tweets
	for i in range(0,10):
		#store tweets appended on each term in a different file
		for term in searchterms_positive:
			filename=datafolder+search_label+'_'+term
			Generate_Tweets(term,filename)

def negative_tweets_collector(datafolder):
	searchterms_positive=['#sad','#gloomy','#depressed','#mourn','#despair']
	search_label='Negative'
	#Repeating tweet collection to get more tweets
	for i in range(0,10):
		#store tweets appended on each term in a different file
		for term in searchterms_positive:
			filename=datafolder+search_label+'_'+term
			Generate_Tweets(term,filename)

if __name__=='__main__':	
	datafolder='data/'
	positive_tweets_collector(datafolder)
	negative_tweets_collector(datafolder)
	


