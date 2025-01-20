import os
import time


log_dir='/home/nraghu'
current_time=time.time()
seven_days_time=7*24*60*60  # taking the 7 days in seconds

print(os.listdir('/home/nraghu')) 

print(os.path.isfile('/home/nraghu/performance_instance')) 

print(os.path.isfile('/home/nraghu/config.xml')) 

for file_name in os.listdir(log_dir):
    file_path=os.path.join(log_dir,file_name)
    if os.path.isfile(file_path): #give True if item is file because listdir will list folder and files of given path
        file_age=current_time - os.path.getmtime(file_path)
        if file_age > seven_days_time:
            print(f"Deleting the file {file_path}")






