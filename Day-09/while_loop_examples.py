
#checking the system startup

'''syntax

while condition:
     code to be executed when condition satisfied and progress of condition must be happen otherwise it will keep on executing infinity time.
else:
    code to be executed when condition not satisfiled

else is optional,we can use the while loop without using else block
'''

import time
import requests

timeout=10
elapsed_time=0
url='http://localhost:9090'

while elapsed_time < timeout:
    try:
        response=requests.get(url)
        if response.status_code == 200:
            print('System is reachable through 8080')
            break
    except requests.ConnectionError:
        print("Waiting for server to star")
    time.sleep(1)
    elapsed_time+=1
else:
    print('Timeout:Server did not start within spicified time')
