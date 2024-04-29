import re

text="Raghu working as DevOps engineer. Raghu have knowlegde on Docker and kubernetes"
pattern=r"Raghu"

#match in re module matches pattern only if pattern found at the beginning of string
match=re.match(pattern,text)

if match:
    print(match.group())
else:
    print("Not found")

