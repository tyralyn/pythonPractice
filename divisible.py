def f():
	l=[]
	comma = ", "
	for i in range (2000,3200):
		if i % 7 == 0 and i % 3 != 0:
			l.append(str(i))
	print (comma.join(l)) #you must declare the comma string rather than just sticking the literal before the join -- why     	
	return;

