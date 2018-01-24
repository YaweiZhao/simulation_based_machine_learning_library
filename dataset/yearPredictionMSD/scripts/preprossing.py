#This python script is used to pre-process YearPredictionSMD
#each sample contains 90 features
import re
import fileinput

def process(str):
	#print("pre-processing...\n")
	pattern = re.compile(':(-?[0-9]+\.?[0-9]*)')
	res=pattern.findall(str)
	count=0
	str=''
	for data in res:
		#if count==0:
		#	count = count+1;
		#	continue''''
		if count==89:
			str=str+data
		else:
			str=str+data+' '
		count = count+1
	if count!=90:
		print("ERROR\n")#verify whether dataset has been parsed correctly
		return -1
	str = str+'\n'
	write2file(str,'train_sample.txt','a+')

def write2file(text, filename2, mod):
	f = open(filename2,mod)
	f.write(text)
	f.close()

def process_label_file(line):
	label=line[:4]
	label=label+"\n"
	write2file(label,'train_label.txt','a+')



filename='YearPredictionMSD'
f = open(filename)
num=0
for line in fileinput.input(filename):
	if len(line)<10:
		continue
	do_right=process(line)
	if do_right==-1:
		break#something goes wrong
	process_label_file(line)
	num=num+1
	precent = 1.0*num/463715
        print(precent)
f.close()


