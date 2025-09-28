# Regex

**1. Regular Expressions for Text Processing:**

- Regular expressions (regex or regexp) are a powerful tool for pattern matching and text processing.
- The `re` module in Python is used for working with regular expressions.
- Common metacharacters:
    . --> any charactor 
    * --> zero or more occurence
    + --> one or more occurence
    ? --> zero or one occurence
    
    [] --> character class --> [A-Z0-9a-z] 
    
    | --> OR operation
    
    ^ start of a line
    
    $ end of a line

    \d --> match any digit(0-9)
    
    most used re is .*
    .*  --> any charactor with zero or more occurence 


how to define pattern?

r"mention the pattern"

ex: r".*zeomega.loc"   --> found words starts with anything but last should have  zeomega.loc

   r"^python"  -->  found words start with python 

   r"$loc"  --> found words ends with  loc

   r"[A-Z]+" --> found if starts with any letter between A to Z that is minimum one or more times
  
   r"\d+"  --> start with any digit with one or more occurence   


| **Pattern**           | **Description**                        | **Example**                     |
|-----------------------|----------------------------------------|---------------------------------|
| `.`                   | Matches any single character (except `\n`). | `r"c.t"` matches `"cat"`, `"cot"`. |
| `^`                   | Matches the start of the string.       | `r"^hello"` matches `"hello world"`. |
| `$`                   | Matches the end of the string.         | `r"world$"` matches `"hello world"`. |
| `*`                   | Matches 0 or more repetitions.         | `r"ab*"` matches `"a"`, `"ab"`, `"abb"`. |
| `+`                   | Matches 1 or more repetitions.         | `r"ab+"` matches `"ab"`, `"abb"`. |
| `?`                   | Matches 0 or 1 repetition.             | `r"ab?"` matches `"a"`, `"ab"`. |
| `[abc]`               | Matches any character in brackets.     | `r"[abc]"` matches `"a"`, `"b"`, `"c"`. |
| `\d`                  | Matches any digit (0-9).               | `r"\d+"` matches `"123"`, `"42"`. |
| `\w`                  | Matches any word character (alphanumeric + `_`). | `r"\w+"` matches `"word1"`. |
| `\s`                  | Matches any whitespace character.      | `r"\s+"` matches spaces or tabs. |


import re

text="Raghu working as DevOps engineer. Raghu have knowlegde on Docker and kubernetes"
pattern=r"Raghu"

#search in re module serach for first occurance of pattern in string, return match if found otherwise None.
search=re.search(pattern,text)

'''When to Use re.search():

Search for a pattern anywhere in a string:

     Use re.search() when you want to find the first occurrence of a pattern in the entire string.

Extract specific substrings:
    If you need to extract a specific part of a string (e.g., email addresses, phone numbers, or dates).

Conditional checks:
    Use it to verify if a pattern exists in a string before proceeding with further logic.
'''

if search:
    #group() gives the pattern
    print(search.group())
    #span() gives the start and end index of pattern found first in text
    print(search.span())
    #start() gives the start index of pattern found first in text
    print(search.start())
    #end() gives the end index of pattern found first in text
else:
    print("Not found")

text = "Order number: #AB1234"
pattern = r"#([A-Z0-9]+)"  # Capture group for alphanumeric order number

match = re.search(pattern, text)

if match:
  order_number = match.groups()[0]  # Access captured group (index 0)
  print("Order number:", order_number)  # Output: Order number: AB1234
else:
  print("No order number found.")


text="Raghu working as DevOps engineer. Raghu have knowlegde on Docker and kubernetes"
pattern=r"Raghu"

#match in re module matches pattern only if pattern found at the beginning of string, otherwise  return None 
match=re.match(pattern,text)
print(match)

if match:
    print(match.group())
else:
    print("Not found")


#findall return the list of all matches of pattern in string

log = "IP: 192.168.1.1, IP: 10.0.0.5"
ips = re.findall(r"\d+\.\d+\.\d+\.\d+", log)
print(ips)  # ['192.168.1.1', '10.0.0.5']


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


#split the given string wherever pattern found and don't include the pattern into new list
data = "user1, user2; user3|user4"
users = re.split(r"[;,|]", data)
print(users)  # ['user1', 'user2', 'user3', 'user4']

#substitute the pattern with given string
config = "server=192.168.1.1"
new_config = re.sub(r"\d+\.\d+\.\d+\.\d+", "127.0.0.1", config)
print(new_config)  # server=127.0.0.1


