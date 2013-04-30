#Stub to call the functions from preprocessTweets and use them on each of the tweets. Generates preprocessed files from the original files

from preprocessTweets import preprocess

def preprocessDoc(filename):
	f=open(filename,'r')
	lines=f.readlines()
	filename=filename+'_pr'
	fw=open(filename,'w')
	for line in lines:
		line=preprocess(line)
		if len(line)!=0:
			line=line+'\n'
			fw.write(line)
			
	
	fw.close()
	f.close()


if __name__=='__main__':	
	#preprocessDoc('test_100')
	preprocessDoc('Negative')
	preprocessDoc('Positive')
	
