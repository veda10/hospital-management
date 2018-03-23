import datetime 
def k(fin,x):
	i=open(fin,"r")
	line=i.readline()
	while(line!=""):	
		words=line.split(" ")
		if x in words:
			print ("DETAILS OF THE PATIENT:")
			print (" ")
			print ("NAME:",end="")
			print (words[0])
			print ("PATIENT ROOM NO.:",end="")
			print (words[1])
			print ("DISEASE:",end="")
			print (words[2])
			print ("SPECIALIST:",end="")
			print (words[3])
			print ("JOINING DATE:",end="")
			print (words[4])
			return 1

		line=i.readline()
	i.close()

def check(fin):
	i=open(fin,"r")
	line=i.readline()
	c1=1
	while(line!=""):	
		c1=c1+1
		line=i.readline()
	return c1
	i.close()
		
def joinpatient(fin):
	i=open(fin,"a")
	print ("NAME:",end="")
	word1=input()
	k=check(fin)
	p=datetime.date.today()
	#p=p.split('-')

	print (p)
	print ("DISEASE:",end="")
	word2=input()
	print ("SPECIALIST:",end="")
	word3=input()
	i.write(word1)
	i.write(" ")
	i.write(str(k))
	i.write(" ")
	i.write(word2)	
	i.write(" ")
	i.write(word3)
	i.write(" ")
	i.write(str(p))
	i.write("\n")
	i.close()
	
def checkdoctor(doctor,name):
	if name in doctor:
		print ("available")
	else:
		print ("doctor not available")
		
def generatebill(fin,name,x):
	i=open(fin,"r")
	line=i.readline()
	while(line!=""):	
		words=line.split(" ")
		if name in words:
			y=words[4]
			#print(x)
			x=str(x)
			p=x.split('-')
			q=y.split('-')
			s=int(p[2])+int(p[1])*30+int(p[0])*365
			s1=int(q[0])+int(q[1])*30+int(q[2])*365
			bill=(s-s1)*(1000+doctor[words[3]])
			return bill
		line=i.readline()
	i.close()

def discharge(fin,d):
	i=open(fin,"r")
	line=i.readline()
	while(line!=""):
		words=line.split(" ")
		if d in words:
			line = line.replace('.' , '')
			return 1
		line=i.readline()
	i.close()

print ("WELCOME To VJS HOSPITAL!!!")
print ("QUERIES:")
print ("1-search patient")
print ("2-join patient")
print ("3-check doctor")
print ("4-bill")
print ("5-discharge patient")
print ("6-quit\n")

#x=0
p=0
doctor={'Dr.Batra':400,'Dr.BalaKrishna':500,'Dr.Harikrishna':600,'Dr.George':300,'Dr.John':350,'Dr.Eugene':450,'Dr.Suzanne':500,'Dr.Mary':550,
'Dr.Peyton':600,'Dr.Richard':380,'Dr.Pearson':320,'Dr.W.Michael':340,'Dr.James':420,'Dr.Paula':480,'Dr.William':400,'Dr.Geoffrey':500,
'Dr.Rajashekhar':600,'Dr.Ramesh':300,'Dr.sirish':350,'Dr.RamaKrishna':450,'Dr.P.SureshKumar':500,'Dr.Avinash':550,'Dr.Arunkumar':600,
'Dr.C.Anil':380,'Dr.P.Pranav':320}
print ("ENTER QUERY")
x=input()
while(x!="6"):	
	if(x=="1"):
		print("ENTER NAME OF THE PATIENT:")
		pt=input()
		p=k("k.txt",pt)
		if(p==None):
			print ("PATIENT DOES NOT EXIST")
		
	elif(x=="2"):
		r=check("k.txt")
		#print(r)
		if(r<120):
			joinpatient("k.txt")
			print("PATIENT ADMITTED")
		else:
			print("hospital full")
		
	elif(x=="3"):
		print("ENTER DOCTOR NAME:")
		b=input()
		checkdoctor(doctor,b)
		
	elif(x=="4"):
		print("ENTER NAME OF THE PATIENT:")
		a=input()
		b=datetime.date.today()
		print("HERE IS YOUR BILL:")
		p=generatebill("k.txt",a,b)
		print(p)
		
	elif(x=="5"):
		print("ENTER NAME OF THE PATIENT:")
		d=input()
		r=discharge("k.txt",d)

		if(r==1):
			print ("Patient discharged")
			b=datetime.date.today()
			print("HERE IS YOUR BILL:")
			p=generatebill("k.txt",d,b)
			print(p)	
		if(r==None):
			print("Patient does not exist")
			
	else:
		print ("INVALID QUERY")
	print("***************************************************************************")
	print ("ENTER QUERY")
	x=input()

