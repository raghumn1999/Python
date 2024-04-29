import sys

#syntax 
'''def name_of_function(arg1,arg2 ....):
       logic for function
       return 
'''

def add(a,b):
    return a+b


def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a%b

#sys.argv[0] sys.argv[1] is like special variables in bash($0 $1 etc)
#sys.argv[0] --> will take python file name as value

#input taken from user in python through argument is always consider ad string,we have to convert into required data type
num1=float(sys.argv[1])
operation=sys.argv[2]
num2=float(sys.argv[3])

if operation=="add":
   print(add(num1,num2))
elif operation=="sub":
   print(sub(num1,num2))
elif operation=="mul":
    print(mul(num1,num2))
elif operation=="div":
    print(div(num1,num2))
else:
    print("Please pass the valid operations as add, sub, mul, div")

