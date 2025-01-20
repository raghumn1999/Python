
import os

#getting the value from env
print(os.environ.get('HOME'))

#setting the environment variable
os.environ["DEPLOY_ENV"]='Production'
print(f'Environment name is {os.environ.get("DEPLOY_ENV")}')

#deleting the environment variable
os.environ.pop('DEPLOY_ENV')
print("DEPLOY_ENV after removal:", os.environ.get("DEPLOY_ENV"))

#====================================================

#getting the current working directory
current_dir=os.getcwd()
print(current_dir)

#changing the directory
os.chdir('/home/nraghu')
print(f'current directory {os.getcwd()}')

os.chdir(current_dir)

#creation of directory
os.makedirs(os.path.join(os.getcwd(),'test'),exist_ok=True)  # exist_ok=True option will not raise error if folder already exist

#list files and folders in given path
print(os.listdir('.'))

#checking file or directory exists
print(os.path.exists('/home/nraghu'))
print(os.path.exists('/home/nraghu/raghu.txt'))

#creation of file
file_path=os.path.join(os.getcwd(),'test.txt')

if not os.path.exists(file_path):
   with open(file_path,'w') as text_file:
        text_file.write('Created the test.txt file')
else:
  print(f'{file_path} is already exists')

#checking is it file, gives True if that is file. same way for directory
print(os.path.isdir('/home/nraghu'))
print(os.path.isfile('/home/nraghu/raghu.txt'))

#delete file
#os.remove(file_path)

#delete directory
path_to_dir=os.path.join(os.getcwd(),'test')
os.rmdir(path_to_dir)
print(f"Files and Folder after deletion are {os.listdir()}")


#Executing the command: os.system(command). on windows os.system() will use cmd.exe and on linux os.system() wil shell

#on linux system
os.system("ls -la | awk 'NR>3'")

#on windows
#os.system('mkdir new_folder')
#os.system('rmdir new_folder')

old_file=os.path.join(os.getcwd(),'old_file.txt')
with open(old_file,'w') as o_file:
    o_file.write('Writing some data')

#renaming the file
os.rename('old_file.txt','new_file.txt')

#changing the permission into file or directory
os.makedirs(os.path.join(os.getcwd(),'raghu'),exist_ok=True)
folder_path=os.path.join(os.getcwd(),'raghu')
file_path=os.path.join(os.getcwd(),'01-most_used_modules_in_python.md')
os.chmod(file_path,0o744)
os.chmod(folder_path,0o777)

#os.stat(file_or_fodler) --> get the details of file or folder
folder_details=os.stat(folder_path)
file_details=os.stat(file_path)

#st_size  --> will give the size information in bytes, we have to conver into MB by dividing 1024*1024 and GB by dividing 1024*1024*1024

# File size in bytes
file_size_bytes = file_details.st_size

# Convert to MB and GB
file_size_mb = file_size_bytes / (1024 * 1024)  # 1 MB = 1024 * 1024 bytes
file_size_gb = file_size_bytes / (1024 * 1024 * 1024)  # 1 GB = 1024 * 1024 * 1024 bytes

# Print the file sizes
print(f"File Size: {file_size_bytes} bytes")
print(f"File Size: {file_size_mb:.2f} MB")
print(f"File Size: {file_size_gb:.4f} GB")
print(f'file size is {file_details.st_size} bytes and modified_time is {file_details.st_mtime}')
print(file_details)

# Get disk usage statistics --> os.statfvs provide the details about the file system such as total size, free space, available space etc
'''f_bfree --> free space means total amount of free space available in system which includes reserved block for privileges (root user)users. 
even through blocks are marked as free,they are not available to normal users.'''
#f_bavail --> available space means space available which can be used by normal users.
'''
Example: Disk with Reserved Space
Disk Size: 100 GB
Reserved Space: 10% (10 GB reserved for root) --> defined standard % to reserve space for root users
Used Space: 80 GB  --> already used from all users in system
Free Space: 100 GB - 80 GB = 20 GB  --> free space mean total space available in system which includes reserved block also.
Available Space for Users: 20 GB - 10 GB (reserved) = 10 GB  --> space available for normal users to use in system
'''
stats = os.statvfs("/")
print(stats)
free_space = (stats.f_bavail * stats.f_frsize) / (1024 * 1024 * 1024)  # Convert to GB
print(f"Free Disk Space: {free_space:.2f} GB")

'''
Devops Perspective:
If "free space" is low, it may indicate the disk is almost full.
If "available space" is low, non-root users or applications may start failing.
'''


