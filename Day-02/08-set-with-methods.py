'''set is a unordered collection of unique elements in python and set is mutable but it element is immutable(eg string,integer,tuple) 
means we add element,remove element into set.
set is used to store data without duplicates'''

#creation of set
tools={'Docker','Jenkins','Kubernetes','Ansible'}

print(tools)

#add() --> adding element to set
tools.add('Terraform')
print(tools)

#remove() --> removing element from set,if element is not present in set,remove will raise the exception.
tools.remove('Jenkins')
print(tools)

#discard() -->  discard is used to remove the element from set even if element not present in set,it will raise exception
tools.discard('Argo CD')
print(tools)

#set is unordered collection right,pop will remove last element from set,pop is not useful bacause set will change the order of element for every execution.
print(f'pop method is',tools.pop())
print(f'elements of set after pop',tools)

#clear and copy work as like how they will work in list and dict

#union(set_name) --> is used to combine the two sets, element is case sensitive.
devops_tools = {"Docker","Kubernetes","Terraform","CI/CD"}
cloud_tools = {"AWS","CI/CD","Azure","kubernetes"}

all_tools=devops_tools.union(cloud_tools)
print(all_tools)


#intersection() --> is used to get set which contains common elements in both sets.
common_tools=devops_tools.intersection(cloud_tools)
print(common_tools)

#set1.difference(set2) --> which will tell how set1 is difference from set2
difference_of_devops_tools=devops_tools.difference(cloud_tools)
print(difference_of_devops_tools)

#devops_tools.symmetric_difference(cloud_tools)  -->  tools either in set but not in both
print(devops_tools.symmetric_difference(cloud_tools))

a={1,2,3}
b={1,2,3,4,5,6}

print(a.issubset(b)) # --> gives true if all elements of set a are available in set b

print(b.issuperset(a)) # --> gives true if set b contain all element of set a and also other elements
