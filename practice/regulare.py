
import re

message='Hi, i am Raghu from Malavalli,Raghu have knolegde on Docker and Kubernetes. Raghu completed CKAD'
pattern=r"Raghu"

print(message)
search_result=re.search(pattern,message)

if search_result:
    print(search_result.span())
    print(search_result.group())
else:
    print('Not found')


message1="Hi Raghu, I am Raghu M N"
message1='AAWSWS'
pattern=r"AWS"

result=re.match(pattern,message1)


if result:
    print("found at beggining")
else:
    print("not found in beggining")


h=re.sub(pattern,'',message1)

print(h)


pattern1=r"\d+"
text="Here are some number 123 764 869"
print(re.findall(pattern1,text))


compiled_pattern=re.compile(pattern1)

print(compiled_pattern.findall(text))

