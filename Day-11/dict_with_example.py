
#creating the dictionary
student_detail={"name":"Raghu","Age":"25","class":"Engineer"}

print(student_detail)

#accessing the element
print(student_detail["name"])

#Adding element
student_detail["Town"]="Malavalli"
print(student_detail)

#creating the nested dictionary

server_details={
        "server1":{"ip":"172.4.53.2","status":"active","port":"7866"},
        "server2":{"ip":"172.4.5.3","status":"inactive","port":"7006"},
        "server3":{"ip":"172.4.2.7","status":"active","port":"8980"}
}

for server_name,other_details in server_details.items():
    print(f"server is {server_name} and details is {other_details}")


def get_server_status(server_name):
    return server_details.get(server_name, {}).get('status', 'Server not found')

# Example usage
server_name = 'server2'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")
