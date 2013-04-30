This folder contains all the scripts used for Collecting and preprocessing the data. 
A short description is availbale below:

> run_hourly.sh: This script runs the tweets_collector.py script after a fixed amount of time. Specifyint the time can get you the tweets for a specific period of time.

>Tweets_collector.py: This script when run, collects utop 100 tweets for each of the hashtags specified in the code. 

> Tpreprocess_remove_search_term.py: This script is run before running the preprocess script. It removes the Hashtag which was used to search the tweet. This is done so that classifier is not biased.

> preprocessTweets.py: This file has all the regex functions to perform the various preprocessing phases in the project. 

> preprocess_stub.py: This file uses the preprocessTweets module to perform the preprocessing on each of the tweet from the initial files and writes it to a new file.

> weka_converter.py: This file takes in the preprocessed filea nd writes it to a csv file which can be read by weka. It escapes all the character which might cause weka to not recognize the file. Thus the output csv file could be used in Weka.


