'''Q.2- Name and handle the exception occurred in the following program:
l=[1,2,3]
print(l[3])'''

'''Answer=> Error Name is =IndexError'''

l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print('Error Detected !')