import re

text="Raghu working as DevOps engineer. Raghu have knowlegde on Docker and kubernetes"
pattern=r"Raghu"

#findall return the list of all matches of pattern in string
search=re.findall(pattern,text)

if search:
    print(search)
else:
    print("Pattern not found")


