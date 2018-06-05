# Program to depict Raising Exception
'''
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print "An exception"
    raise  # To determine whether the exception was raised or not
'''

'''Answer2.=> According to python 3.x
                SyntaxError: Missing parentheses in call to print
              According to python 2.x
                The output would be:
                NameError: Hi there  
                '''