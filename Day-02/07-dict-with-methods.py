'''Dictionary is collection of key-value pair,mutable.
Each key in dictionay must be unique and keys are immutable,we can modify the value using built-in methods.
'''

devops_tools={
        'CI/CD':'Jenkins',
        'Containerization':'Docker',
        'Orchestration':'Kubernetes',
        'Script language': 'Shell Script' 
        }

#accessing the vaule using key
print(devops_tools['Containerization'])

#adding new key value pair
devops_tools['Monitoring']='Prometheus'

#updating vaule
devops_tools['CI/CD']='GitLab'

#removing the element from dictionary
del devops_tools['Orchestration']

#built-in methods

#get(key) --> getting the value from key
print(devops_tools.get('Monitoring'))

#keys() --> getting the keys from dict
print(devops_tools.keys())

#values() --> getting the values from dict
print(devops_tools.values())

#items() --> gives the object containing key value pair as tuple
print(devops_tools.items())

#pop(key) --> deleting the key value using key
print(devops_tools.pop('CI/CD'))

#popitem() --> deleting the last key value from dictionary
print(devops_tools.popitem())

new_tools={
        'new_CD':'Argo CD',
        'Graphical monitoring tool':'Graphana'
        }

#update --> update dictionary with the key value pairs from another dictionary
devops_tools.update(new_tools)

print(devops_tools)

#copy() --> copy is used to copy dict into other
copied_devops_tools=devops_tools.copy()
print(copied_devops_tools)

#clear() --> clear is used to remove the key value pair from dict
devops_tools.clear()
print(devops_tools)

def configure_pipeline(config):
    for key, value in config.items():
        print(f"Setting {key} to {value}")

pipeline_config = {
    "Build Tool": "Maven",
    "Testing Framework": "JUnit",
    "Deployment": "Kubernetes"
}

configure_pipeline(pipeline_config)

