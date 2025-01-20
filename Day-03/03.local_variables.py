def addition(x,y):
    #local variables x and y
    print(x)
    print(x+y)

addition(4,7)



#using the globally defined variable inside of funtion

name='Raghu'

def greeting():
    global name
    print(f'Hi, I am {name}, welcome to Green Hotel')

greeting()
