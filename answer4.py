# Driver program to test function given below in program
#AbyB(2.0, 3.0)
#AbyB(3.0, 3.0)

 # Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)

'''
OUTPUT WOULD BE:
-5.0
a/b result in 0
'''