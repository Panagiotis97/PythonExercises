imerominia=raw_input("Parakalw eisagete tin imerominia se morfh dd/mm/yyyy:")
imerominia=imerominia.split("/")
#kataxwrisi metavlitwn
day=int(imerominia[0])
month=int(imerominia[1])
year=int(imerominia[2])
month = (month + 9) % 12
year = year - month/10
mera= 365*year + year/4 - year/100 + year/400 + (month*306 + 5)/10 + ( day - 1 )



final = mera%7
final=final+3
#euresi imeras

if final==0:
	print "Kiriaki"
elif final==1:
	print "Deutera"
elif final==2:
	print "Triti"
elif final==3:
	print "Tetarti"
elif final==4:
	print "Pempti"
elif final==5:
	print "Paraskeui"
elif final==6:
	print "Savvato"
elif final==7:
	print "Kiriaki"
elif final==8:
	print "Deutera"
elif final==9:
	print "Triti"
	

