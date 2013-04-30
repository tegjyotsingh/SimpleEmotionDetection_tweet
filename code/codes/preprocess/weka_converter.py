# Converting Preprocessed files to a cvs format suitable to be used in Weka. Adds necessary class labels, headers, ecsape characters,etc.
import re

def weka_compatible(line,tclass):
	line=line.strip()
	line=re.sub(r'\\','',line)
	line=re.sub(r'%','',line)
	line='\''+line+'\''+','+'\''+tclass+'\''+'\n'
	return line
	
def Convert_weka(filename,tclass,fw):
	f=open(filename,'r')
	lines=f.readlines()
	
	
	for line in lines:
		line = re.sub(r"'","",line)
		if len(line)!=0:
			line=weka_compatible(line,tclass)
			fw.write(line)	
	
	f.close()


if __name__=='__main__':
	Output_file='Weka_compatible.csv'
	fw=open(Output_file,'w')
	fw.write('Text,Class\n')	
	Convert_weka('Negative_pr','Neg',fw)
	Convert_weka('Positive_pr','Pos',fw)
	fw.close()
	
