#Files containing preprocessing functions to be used on each tweet
import re
# test tweet:  tweet='RT 1 billion RT HAPPY @xyay: #sad #gotohell, how are you? when. YESSSSSSS 1123q       12qw qw' 

# removing RT for Re tweets from start of some tweets
EMOTICON_LIST={':)':'PosEmoti',':-)': 'PosEmoti',':o)': 'PosEmoti',':]': 'PosEmoti',':3': 'PosEmoti',':c)': 'PosEmoti',':D':'PosEmoti','C:':'PosEmoti',';)':'PosEmoti', ':}':'PosEmoti', ':8':'PosEmoti',':(':'NegEmoti',':-(': 'NegEmoti',':c':'NegEmoti',':C':'NegEmoti' ,'D8':'NegEmoti','D;':'NegEmoti','D=':'NegEmoti','DX':'NegEmoti','v.v':'NegEmoti',':-D':'NegEmoti',':<':'NegEmoti',':{':'NegEmoti','D:':'NegEmoti','D:':'NegEmoti',';(':'NegEmoti',
':\'(':'NegEmoti','<3':'HEART','</3':'BROKEN_HEART'}

def remove_RT(tweet):
	tweet = re.sub(r'^RT','',tweet)
	tweet = re.sub(r'\bRT\b','',tweet)
	return tweet

#converting Tweets to lower cases
def convert_tolower(tweet):
	tweet=tweet.lower()
	return tweet

#Convert @username to AT_USER
def remove_username(tweet):
	#tweet = re.sub('@[^\s]+','AT_USER',tweet)
	tweet = re.sub('@[^\s]+','',tweet)
	return tweet

#remove URLS
def remove_URLS(tweet):
        #tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))','URL',tweet)
        tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))','',tweet)
	return tweet

#remove Hashtags and keep only word.
def remove_hash(tweet):
	#Replace #word with word
    	tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
	return tweet

# remove symbols and keep only the words. [, . ? ! _ - "]
def remove_symbols(tweet):
	tweet = re.sub(r'[,.?/\<>*\(\)!_-]',' ',tweet)
	tweet = re.sub(r'\"','',tweet)
	tweet = re.sub(r"'",'',tweet)
	return tweet

def remove_symbols_new(tweet):
	tweet = re.sub(r"'",'',tweet)
	tweet = re.sub(r'\W',' ',tweet)
	tweet = re.sub(r'_',' ',tweet)
	return tweet
# REMOVE words starting with numbers
def remove_numbers(tweet):
	tweet = re.sub(r'\s(\d[^\s]*)','',tweet)
	tweet = re.sub(r'^\d[^\s]*','',tweet)
	return tweet

#Remove additional WhiteSpaces
def remove_whitespaces(tweet):
	tweet = re.sub(r'[\s]+',' ',tweet)
	tweet = tweet.strip()
	return tweet

 #look for 2 or more repetitions of character and replace with the two of the characters
def replaceTwoOrMore(tweet):
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", tweet)

def replaceEmoticons(tweet):
	for i in EMOTICON_LIST.keys():
		paddedEmoti=" "+EMOTICON_LIST[i]+" "
		pattern_search=re.escape(i)
		tweet=re.sub(pattern_search,paddedEmoti,tweet)
	return tweet
	
#Preprocessing stub
def preprocess(tweet):
	processed_tweet=replaceTwoOrMore(remove_whitespaces(remove_numbers(remove_symbols_new(remove_hash(remove_URLS(remove_username(convert_tolower(replaceEmoticons(remove_RT(tweet))))))))))
	return processed_tweet
