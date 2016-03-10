import urllib2
from bs4 import BeautifulSoup

#Eisagwgi twn 2 onomatwn
print ("Parakalw eisagete ta 2 onomata twn logariasmwn sto twitter")
name1=raw_input("@")
name2=raw_input("@")
print ("Tha parei ligh wra..")

#antistoixisi onomatwn sta katallila profile link
url1="https://twitter.com/"+name1
url2="https://twitter.com/"+name2

#gia ton prwto
page1=urllib2.urlopen(url1).read()
soup1=BeautifulSoup(page1)
data1=soup1.findAll("span",{ "class" : "ProfileNav-value"})
numbers1= [d.text for d in data1]

#kataxwrisi stoixeiwn tou prwtou se metavlites
tweets1=numbers1[0]
following1=numbers1[1]
followers1=numbers1[2]
likes1=numbers1[3]

#gia ton deutero
page2=urllib2.urlopen(url2).read()
soup2=BeautifulSoup(page2)
data2=soup2.findAll("span",{ "class" : "ProfileNav-value"})
numbers2 = [d.text for d in data2]

#kataxwrisi stoixeiwn tou deuterou se metavlites
tweets2=numbers2[0]
following2=numbers2[1]
followers2=numbers2[2]
likes2=numbers2[3]

#ipologismos skor
score1=0
score2=0
if tweets1>tweets2	:
	score1=score1+1
elif tweets1<tweets2:
	score2=score2+1
	
if following1>following2 :
	score1=score1+1
elif following1<following2 :
	score2=score2+1

if followers1>followers2 :
	score1=score1+1
elif followers1<followers2 :
	score2=score2+1
	
if likes1>likes2 :
	score1=score1+1
elif likes1<likes2 :
	score2=score2+1
	
	
	

print 'To score einai', score1, '-', score2
