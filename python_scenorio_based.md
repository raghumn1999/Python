# 1) Used Python in day to day activity?
* I have written the python script to create the docker container for developer
* I have used docker skd in python to do this

```
import docker

# Initialize Docker client
client = docker.from_env()

# Get image name from user input
image_name = input("Enter the Docker image name (e.g., nginx:latest): ").strip()

try:
    # Pull the image (if not present locally)
    print(f"Pulling image '{image_name}'...")
    client.images.pull(image_name)
    print(f"Image '{image_name}' pulled successfully.")

    # Run the container
    print(f"Running container from image '{image_name}'...")
    container = client.containers.run(image_name, detach=True)
    print(f"Container started with ID: {container.id[:12]}")

except docker.errors.ImageNotFound:
    print(f"Error: Image '{image_name}' not found.")
except docker.errors.APIError as e:
    print(f"Docker API error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

# 2) What are some common packages that you use as a DevOps Engineer?
* DevOps Engineers often use Python for scripting, automation, cloud interactions, and infrastructure management. 
* Some commonly used Python packages for DevOps Engineers include boto3, paramiko, requests, pyyaml, docker, kubernetes, fabric, and pytest.

## Detailed explanation (with examples)

1. **boto3** – AWS SDK for Python  
   Used to automate and manage AWS services.
   
```
   Example:
       import boto3
       ec2 = boto3.client('ec2')
       response = ec2.describe_instances()
       print(response)
```

2. **paramiko** – SSH and remote command execution  
   Useful for running remote shell commands or transferring files via SFTP.
   
```
   Example:
       import paramiko
       ssh = paramiko.SSHClient()
       ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       ssh.connect(hostname='remote.server.com', username='user', password='pass')
       stdin, stdout, stderr = ssh.exec_command('uptime')
       print(stdout.read().decode())
       ssh.close()
```

3. **requests** – HTTP requests  
   Used for interacting with REST APIs and webhooks.

```
   Example:
       import requests
       response = requests.get('https://api.example.com/status')
       print(response.status_code)
       print(response.json())
```

4. **pyyaml** – YAML parsing and generation  
   Very useful when dealing with Kubernetes manifests or configuration files.

```
   Example:
       import yaml
       with open('config.yaml', 'r') as file:
           config = yaml.safe_load(file)
       print(config)
```

5. **docker** – Docker SDK for Python  
   Used to manage Docker containers, images, and volumes programmatically.

```
   Example:
       import docker
       client = docker.from_env()
       for container in client.containers.list():
           print(container.name, container.status)
```

6. **kubernetes** – Kubernetes Python client  
   Helps in automating Kubernetes resource creation, deletion, and monitoring.

```
   Example:
       from kubernetes import client, config
       config.load_kube_config()
       v1 = client.CoreV1Api()
       pods = v1.list_pod_for_all_namespaces()
       for pod in pods.items:
           print(pod.metadata.name)
```

7. **fabric** – High-level SSH command execution  
   Simplifies automation tasks on remote servers.

```
   Example:
       from fabric import Connection
       c = Connection('user@host')
       c.run('uname -a')
```

8. **pytest** – Python testing framework  
   Useful for writing automated tests for infrastructure or config scripts.

```
   Example:
       def add(a, b):
           return a + b

       def test_add():
           assert add(2, 3) == 5
```
# 3) Find and print 400 error logs from a Logfile?
* Use Python’s requests library to fetch the log file from a public URL and filter for lines containing 404
* 
```
import requests

# Publicly available Apache log sample
log_url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/apache_logs/apache_logs'

try:
    # Fetch the log content
    response = requests.get(log_url)
    response.raise_for_status()
    logs = response.text.splitlines()

    print("Log lines with 404 Not Found:\n")

    # Search for lines with HTTP 404
    for line in logs:
        if ' 404 ' in line:
            print(line)

except requests.exceptions.RequestException as e:
    print(f"Error fetching logs: {e}")
```

