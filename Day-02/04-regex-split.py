import re

fruits="apple:orange:mango:graps"

pattern=r":"

#split the given string wherever pattern found and don't include the pattern into new list
new_fruits=re.split(pattern,fruits)

print(new_fruits)
