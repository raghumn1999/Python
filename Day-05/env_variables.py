#export the env on terminal,use getenv to get value

import os

print(os.getenv("password"))

#=====================================================================

'''if we want read multiple env,install python-dotenv python package.
create .env file in directory where python scripts are placed.

In python script,import load_dotenv function from dotenv
'''

import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv('DB_USER'))
print(os.getenv('DB_PASSWORD'))



