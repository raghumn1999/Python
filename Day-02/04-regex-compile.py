import re

pattern=r"\d+"

#compile in re module is used compile the pattern for reusability. 
#reusability means instead of using pattern  in evey re functions(search,match etc),we can use the compiled regex pattern.
#compiled pattern is then used for all other functions

compiled_pattern=re.compile(pattern)
print("compiled pattern is ",compiled_pattern)
text="Here are some number 123 764 869"

#now we can use the complied_pattern in any functions of re module
found_numbers=compiled_pattern.findall(text) #Equivalent to re.findall(r"\d+", text)
print(found_numbers)
print(compiled_pattern.search(text).group())
print(compiled_pattern.match(text))

# Compile pattern with case-insensitive flag
pattern = re.compile(r"python", re.IGNORECASE)

text = "I love Python programming."

# Search for the pattern
match = pattern.search(text)
if match:
    print("Match found:", match.group())
