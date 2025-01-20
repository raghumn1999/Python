
'''
Relational operator are used to compare two values and get the result.
Logical operator is used to check two vaule which are True or False.

Relational operation performed first,then logical operation performed.
See the below example

'''
result = 3 < 5 and 5 > 2
print(result)  # Output: True (Comparison operators are evaluated before `and`)

#monitoring the servers

servers={
        'server1':{'cpu_usage':85,'memory_usage':69,'disk_usage':50},
        'server2':{'cpu_usage':90,'memory_usage':80,'disk_usage':40},
        'server3':{'cpu_usage':60,'memory_usage':75,'disk_usage':60},
        'server4':{'cpu_usage':78,'memory_usage':90,'disk_usage':80},
        'server5':{'cpu_usage':50,'memory_usage':60,'disk_usage':40}
        }

#relational operator evaluted first,then logical operator will evaluate 
for server,server_data in servers.items():
    if server_data['cpu_usage'] >= 90 or server_data['memory_usage'] >= 85 or server_data['disk_usage'] >= 80:
        print(f'{server} need the attention')
    else:
        print(f'{server} is in good condition')




# Example: Categorize employees based on performance criteria
employees = [
    {"name": "Alice", "hours_worked": 45, "projects_completed": 5},
    {"name": "Bob", "hours_worked": 30, "projects_completed": 2},
    {"name": "Charlie", "hours_worked": 40, "projects_completed": 3},
]

# Performance categories
for employee in employees:
    if employee["hours_worked"] >= 40 and employee["projects_completed"] >= 4:
        category = "Excellent"
    elif employee["hours_worked"] >= 40 or employee["projects_completed"] >= 4:
        category = "Good"
    else:
        category = "Needs Improvement"
    
    print(f"{employee['name']} is in the '{category}' category.")



#not --> is used to reverse the result in python

