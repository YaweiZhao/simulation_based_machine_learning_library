import fileinput

def write2file(text, filename2, mod):
	f = open(filename2,mod)
	f.write(text)
	f.close()

def normal_label():#the label 'year' ranges from 1922 to 2011
	print("processing normal_label....")
	range=2011-1922
	filename='C:\\Users\\Yawei\\Desktop\\train_label.txt'
	f=open(filename)
	count=0
	for line in fileinput.input(filename):
		count=count+1
		year_normal = 1.0*(float(line)-1922)/range
		str1=''
		if count == 463715:
			str1=str(year_normal)
		str1=str(year_normal)+'\n'
		write2file(str1,'C:\\Users\\Yawei\\Desktop\\train_label_normal.txt','a+')
	f.close()

def normal_sample():
	print("processing normal_sample....")
	#max=-999999999999.0
	#min=99999999999.0
	sample_list=[]
	filename='train_sample.txt'
	f=open(filename)
	#for line in fileinput.input(filename):
	#	if line.find('\n')==-1:
	#		weight_list=line.split(' ')
	#	else:
	#		ind=line.find('\n')
	#		weight_list=line[:ind].split(' ')
	#	for elm in weight_list:
	#		#print(elm)
	#		if max<float(elm):
	#			max=float(elm)
	#		if min>float(elm):
	#			min=float(elm)
	max=65735.78125
	min=-14861.695312
	num=0
	for line in fileinput.input(filename):
		num=num+1
		sample_list=[]
		if line.find('\n')==-1:
			weight_list=line.split(' ')
			#print('......................')
		else:
			index=line.find('\n')
			weight_list=line[:index].split(' ')
		count=0
		#print(weight_list)
		for elm in weight_list:
			#print("the last elm:",elm)
			elm_normal=1.0*(float(elm)-min)/(max-min)
			#print(elm_normal)
			#count=count+1
			sample_list.append(elm_normal)
			#sample_list.append(' ')
		content=''
		count=0
		#print("the last elm:",weight_list[89])
		for elm in sample_list:
			count=count+1
			if count==90:
				#print("last one:",elm)
				#return;
				content=content+str(elm)
			else:
				content=content+str(elm)+' '
		#if(num<463715):
		#	content=content+'\n'
		#print(num)
		content=content+'\n'
		write2file(content,'train_sample_normal.txt','a+')
		#print(1.0*num/463715)
	#print("max=%f,min=%f", max,min)


#normal_label()
normal_sample()
