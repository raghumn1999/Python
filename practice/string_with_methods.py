Name='Raghu M N'

#indexing
print(f'Fisrt letter of Name is {Name[0]}')

print(f'Last letter of Name is {Name[-1]}')

print(Name[2])

#slicing
print(Name[:2])

print(Name[2:])

print(Name[2:5])

#finding length of string
print(len(Name))

print(Name.split(" "))

print(Name)

message1='Hello'
message2='Raghu M N'
print(message1+message2)


print(message1.upper())

print(message2.lower())

City_Name='malavalli'
print(City_Name.capitalize())

Father_Name='   Nagendra M N       '
print(Father_Name.strip())

text='Python is awesome'
modified_text=text.replace('awesome','great')
print(modified_text)


if text.startswith('Python'):
   print('Text is starting with python')
else:
   print('Text is not starting with python')

if text.endswith('awesome'):
   print('Text is ends with awesome')
else:
    print('Text is not ends with awesome')



