
#string methods

info="HI, I am Raghu, I came from Malavalli Mandya"

print(info[4])
print(info[0])
print(info[-1])


print(len(info))

print(info[:5])
print(info[6:])

print('Hello'+'Message')

print(info.upper())
print(info.lower())
print(info.capitalize())


name=' Raghu M N      '
print(name.strip())
print(name.split('a'))

print(name.replace('a','z'))

if info.startswith('Hi'):
   print(f'Yes message is starts with Hi')
else:
    print("No messgae is not starts with Hi")

if info.endswith('Malavalli'):
   print(f'Yes message ends with Malavalli')
else:
    print('No message is not ends with Malavalli')

x=[1,3,4]
y=[1,3,4]


result= x is y
print(result)


fruits=['apple','kiwi','banana']

checking_banana='banana' in fruits
if checking_banana:
    print('Banana is available in fruits list')

checking_orange='orange' not in fruits
if checking_orange:
    print('Orange is not available in fruits list')
