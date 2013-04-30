import re
#function to remove the term which was used for searching the term
folder="cleaned_data/"
def remove_term(tweet,term):
	# fourth argument is count given as 0 so as to match all terms
	tweet=re.sub(term,'',tweet,0,re.IGNORECASE)
	return tweet

def clean_file(filename,term):
	f=open(filename,"r")
	fw=open(filename+"_clean","w")

	lines=f.readlines()
	for line in lines:
		tweet=remove_term(line,term)
		fw.write(tweet)
	
	f.close()
	fw.close()

if __name__=='__main__':
		
	terms=["#depressed", "#despair","#sad","#gloomy","#mourn"]
	prefix="N_"
	for i in terms:
		clean_file(prefix+i,i)

	terms=["#happy", "#merry","#joy","#ecstatic","#bliss"]
	prefix="P_"
	for i in terms:
		clean_file(prefix+i,i)
