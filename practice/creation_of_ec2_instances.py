
import sys

ec2_type=sys.argv[1]

if ec2_type.upper()=="GENERAL_PURPOSE":
    print('Created the General Purpose EC2')
elif ec2_type.upper()=="STORAGE_OPTIMIZED":
    print('Created the Storage Optimized EC2')
elif ec2_type.upper()=="MEMORY_OPTIMIZED":
    print('Created the Memory Optimized EC2')
else:
    print('EC2 instance type is invalid')
