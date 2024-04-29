import re

pattern=r"\d+"

#compile in re module is used compile the pattern for reusability.
#compiled pattern is then used for findall method.
compiled_pattern=re.compile(pattern)
print(compiled_pattern)

text="Here are some number 123 764 869"
found_numbers=compiled_pattern.findall(text)
print(found_numbers)

print(compiled_pattern.search(text).group())


