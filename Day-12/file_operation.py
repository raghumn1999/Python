
def update_server_conf_file(file_path,key,value):

    #reading the content of file as lines and storing as list

    with open(file_path, "r")  as file:
         lines = file.readlines()

    #opening file in writing mode to write content
    with open(file_path, "w") as file:
         for line in lines:
             if key in line:
                file.write(key + "=" + value + "\n")
             else:
                 file.write(line)


# Path to the server configuration file
server_config_file = 'server.conf'

# Key and new value for updating the server configuration
key_to_update = 'MAX_CONNECTIONS'
new_value = '1500'  # New maximum connections allowed

update_server_conf_file(server_config_file, key_to_update, new_value)
            
