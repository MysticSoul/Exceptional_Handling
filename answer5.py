'''Q.5- Write a program to show and handle following exceptions:
1. Import Error
2. Value Error
3. Index Error'''

from math import *

try:

    l = [1, 2, 3, 4, 5]
    a = int(input('Enter an Number: '))
    print(factorial(a))
    print(l[a])
    from Harshit import *

except ImportError:
    print("Error Handled")

except ValueError:
    print("You are allowed to enter integers value only")

except IndexError:
    print("Index Error Encountered")