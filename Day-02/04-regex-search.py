import re

text="Raghu working as DevOps engineer. Raghu have knowlegde on Docker and kubernetes"
pattern=r"Raghu"

#search in re module serach for first occurance of pattern in string, return match if found otherwise None.
search=re.search(pattern,text)

if search:
    print(search.group())
    print(search.span())
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
