'''a=3
 if a<4:
    a=a/(a-3)
     print(a)

if we will rum that above code then ZeroDivisionError Arises.
and
The Solution of the above Code is given Below
'''
try:
	a=3
	if a<4:
		a=a/(a-3)
		print(a)
except ZeroDivisionError:
	print('Division by Zero is Not Possible')