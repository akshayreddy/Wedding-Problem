
import sys
FileName=sys.argv[1]
N=int(sys.argv[2])
print N
Content=open(FileName,"r+")             #Retriving the friend's list
count,string,l,n,h,z,placed=0,"",[],[],[],[],[]

for lines in Content:
	l.append(lines.split())
Content.close()

for x in l:
	n=n+x
	h.append(x[0])

AllPeople=set(n)
AllPeople=list(AllPeople)

#making a dictionary of all the people and there immediate freinds  

for x in AllPeople:
	if x in h:
		z.append({'RootName':x,'ImmediateFriends':l[h.index(x)][1:],'Table':[]})
	else:
		z.append({'RootName':x,'ImmediateFriends':[],'Table':[]})       #if person has no immediate friends 

for x in z:
	print x

print "\n\n\n"


for x in z:
	if x['RootName'] not in placed:
		for y in z:
			if len(x['Table'])<N:
				if x['RootName'] not in y['ImmediateFriends'] and y['RootName'] not in placed and \
				   y['RootName'] not in x['ImmediateFriends']:
				   placed.append(y['RootName'])
				   x['Table'].append(y['RootName'])

	
	for m in x['Table']:
		if m in h:
			for n in x['Table']:
				if n in l[h.index(m)][1:]:
					placed.remove(n)
					x['Table'].remove(n)

for x in z:
	if x['Table']!=[]:
		count=count+1
		string=string+",".join(x['Table'])+" "

print "%d %s"% (count,string)


#Storing It in a list FriendsList
#RootFriend
#Immediate friends 
#Unknows persons