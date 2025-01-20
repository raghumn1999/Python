
import time
import os

#time.time() return the current time in seconds since Epoch(unix timestamp)
print(time.time())

#convert the timestamp into human readable format
print(time.ctime(time.time()))

#time.sleep(seconds) --> pause the execution for mentioned seconds
print('waiting for 2 seconds')
time.sleep(2)
print('done')

#time.localtime() --> convert timestamp into local time zone
time_in_local_zone=time.localtime(time.time())
print(f'Time in local zone is {time_in_local_zone}')


#to convert the time into human readable format
#time.strftime(format,time_in_local_zone)

time_in_seconds=time.time()
time_in_local=time.localtime(time_in_seconds)
readable_format=time.strftime("%Y-%m-%d %H-%M-%S",time_in_local)
print(readable_format)

#checking the last modified time of file in human readable format
file_details=os.stat(os.path.join(os.getcwd(),'02-os-module-examples.py'))
modified_time_of_file=file_details.st_mtime
#st_mtime means last modified time and st_ctime means creation time and st_atime means last access time(read file but not changes any content)
#we can use time.strftime(format,time_in_localtime) -->  in this method we know the how we are print the time details 
convert_mtime_to_local_zone=time.localtime(modified_time_of_file)
readable_time_format=time.strftime("%Y-%m-%d %H-%M-%S",convert_mtime_to_local_zone)
print(f'file modified time is {readable_time_format}')

#we can use the time.ctime(time_in_seconds) gives time details in human readable format 
modified_time_of_file=file_details.st_mtime
print('getting time format using time.ctime() method',time.ctime(modified_time_of_file))

#checking the files which created before 24 hour
# Directory to monitor
directory_path = "/var/log"

# Get the current time
current_time = time.time()

# Threshold (e.g., file created in the last 24 hours)
time_threshold = current_time - (24 * 60 * 60)

# List files with recently changed metadata
print(f"Files with metadata changes in the last 24 hours in '{directory_path}':")
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.isfile(file_path):
        file_stat = os.stat(file_path)
        if file_stat.st_ctime > time_threshold:
            formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(file_stat.st_ctime))
            print(f"{filename} - Metadata Changed: {formatted_time}")

