import re

text="Raghu M N working as DevOps engineer in Zeomega and Raghu M N is from Malavalli"
pattern=r"Raghu"

new_text=re.sub(pattern,"Ravi",text)

print(new_text)
