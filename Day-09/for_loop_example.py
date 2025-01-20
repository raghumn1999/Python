#checking the servers status

import os
servers=["192.168.1.1", "192.168.1.2", "192.168.1.3"]

for server in servers:
    response=os.system(f"ping -c {server} > /dev/null 2>&1")
    if response == 0:
       print(f"{server} is reachable")
    else:
        print(f"{server} is unreachable")

'''
The break down of ping -c {server} > /dev/null 2>&1  

* /dev/null is special file in unix/linux system. that discard all data written to it.

* the std output of ping command writting into /dev/null and std error of ping command is redirecting to std output
'''

#==============================================================================================================

required_files=['app.txt','log.txt','error.txt']
deployment_dir='/home/test/application'

for file in required_files:
    path_to_file = os.path.join(deployment_dir,file)
    if os.path.exists(path_to_file):
        print(f"{file} is available under {deployment_dir} dir")
    else:
        print(f"{file} is not available under {deployment_dir} dir")

#==============================================================================================================

#printing the old numbers
for n in range(10):
    remainder=n%2
    if remainder == 0:  #continue statment will skip code execution in if block when condition meet
        continue
        print('This will not be printed')
    else:
       print(n)

#==============================================================================================================

threshold=5
for count in range(6):
    if count == threshold:
        print('Threshold is reached')
        break  #break will exit from loop,whehn condition is meet
    else:
        print(f"current count is {count}")

    
