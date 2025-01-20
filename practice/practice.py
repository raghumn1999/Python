#Numeric data type
Age=26

Marks=10.5

print(f'my age is {Age} and float is {Marks}')

#sequence data type

#string 
Message='Hello this is Raghu from Malavalli'
print(f'Message from Raghu is {Message}')


#list--> ordered,mutable
my_details=['Raghu',26,'Malavalli']
print(my_details)

#tuple--> ordered, immutable(can't update data into tuple)
admin_details=('Admin@123','Nagendra@123','Naga@123')
print(admin_details)

#dictionary --> key-value store
proper_details={'Name':'Raghu M N','Age':26,'Town':'Malavalli'}
print(proper_details)

#set and frozenset
set_numbers={1,2,3}
print(set_numbers)

unmodified_numbers=frozenset({1,2,3,4,5})
print(unmodified_numbers)

#boolean
#True False

#binary data type
byte=b'Hello'
b=bytearray(b'hello')
print(byte)
print(b)


