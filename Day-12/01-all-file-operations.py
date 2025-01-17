# Reading a file line by line. Below both  methods will work fine,i will go with first method(readlines())

with open("read_example.txt", "r") as file:
    lines=file.readlines() #gives result in list,each line will be element of list
    for line in lines:
        print(line.strip())

with open("read_example.txt", "r") as file: # gives result TextIOWrapper ,we can print the each line,we can access
    for line in file: 
        print(line.strip())


#writing into file. if file is exists overwrite the content otherwise create and write content

with open('write_example.txt','w') as w_file:
    w_file.write('Hi I am Raghu')


#Appending content into file --> open file for appending content, if not present create and write content

with open('append_example.txt','a') as a_file:
    a_file.write("Adding the some data into file \n")

# Extracting errors from a log file
with open('app.log','r') as app_log, open('error.log','w') as error_log:
    for line in app_log:
        if 'Error' in line:
            error_log.write(line)
print("Error log extracted to error.log.")


#x mode --> create file for writing, fails if the file already exits. x mode not really required.

#t mode --> text mode, it is default mode in python file operation,used with w,r,a modes.
#it will not really matter if don't mention it as 'wt' --> write in text mode, 'rt' and 'at'.


#b mode --> binary mode used with read,write and append modes
#for writing binary data to image file or reading from image


# Writing binary data to a file
binary_data = b'\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64'  # "Hello World" in bytes

with open("example.bin", "wb") as file:
    file.write(binary_data)
print("Binary file written successfully.")


# Copy an image file
with open("source_image.jpg", "rb") as src_file:
    binary_data = src_file.read()

with open("copy_image.jpg", "wb") as dest_file:
    dest_file.write(binary_data)

print("Image file copied in binary mode.")





