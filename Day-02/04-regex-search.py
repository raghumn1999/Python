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
