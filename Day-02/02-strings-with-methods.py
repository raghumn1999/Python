Name="Raghu M N"
#indexing --> starts zero from leftside and start from -1 from rightside
print(f'Fisrt letter of Name is {Name[0]}')
print(f'Last letter of Name is {Name[-1]}')

print("="*30)

#if don't mention any indexing value in starting --> it will consider zero as default for starting index
#and it will not print 4th index value of string
print(Name[:4]) 
print(Name[2:-1])
print(Name[2:])

# AAWSWSA  --> iterate over the string,remove formation of AWS from given string and keep remaining.

#f formatting --> combining the string with varibles to complete statement.
#f formating will support single quotes,double quotes and trible quotes.
#i always go with double quotes
Name="Ravi M N"
work="DevOps Engineer"
print(f"i am {Name}, i am working as {work}")
print("="*30)

#spliting the string with space --> split()
#the output generated using built-in function of string will not be stored in same variable,we have declare different variable
print(Name.split(" "))
print("="*30)

# len() --> it will consider all lettter and special charactors
print("Counting the number letter in Name -->", len(Name))
print("="*30)

# +  --> concate
Message1="Hello"
Message2="World"
print(Message1 + " " + Message2)
print("="*30)

#upper()
print(Message1.upper())
print("mass_699".upper())

#lower()
print(Message2.lower())
print("MASS_87".lower())

#capitalize --> make only first letter of staring word capital and other words are small letters
print(Message1.capitalize())
print("="*30)

#title() --> make first letter of each word in capital letters
name="Raghu from malavalli"
print(name.title())

#strip --> will remove the space in begining and ending of string and give only string
print("   Nagendra ".strip())

#escape sequence
print("Hi \"Raghu\" what are you doing")

#replace(old_value,new_value)
text="Python is awesome"
print(f"Old text ====>  {text}")
modified_text=text.replace("awesome","great")
print(f"Modified text ==>  {modified_text}")

#startswith("string which need to check in start")
if text.startswith("Python"):
    print("text starts with Python word")
else:
    print("text not start with Python word")

#endswith("string which need to check in end")
if text.endswith("awesome"):
    print("text ends with awesome word")
else:
    print("text not ends with awesome word")


