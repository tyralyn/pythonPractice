def f():
	l=[]
	for i in range (2000,3200):
		if i % 7 == 0 and i % 3 != 0:
			l.append(str(i))
	print (l)      	
	return;