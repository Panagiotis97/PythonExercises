import urllib2
import json
print "Dwse tis sintetagmenes x,y:"
lon=input("Dwse x:")
lat=input("Dwse y :")
#arxikopoihsh twn x kai y
x=lon
y=lat
#link gia to openweathermap
link='http://api.openweathermap.org/data/2.5/weather?lat=%d&lon=%d&appid=f204ad1f1f80eeea5bb29cac8d0f895f' %(y,x)
#sindesi me to link
page=urllib2.urlopen(link)
data=json.load(page)
#antistoixish metavlitwn
kairos=data["weather"][0]["main"]
#emfanish mhnumatwn
if kairos== "Rain":
	print "I'm singing in the rain!"
	
thermokrasia=data["main"]["temp"]
therm_kelsiou=thermokrasia/274.15
if therm_kelsiou > 20 :
	print  "nice..."
elif therm_kelsiou < 5:
	print  "brrrr"
	
