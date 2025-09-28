#list is ordered collection of elements and which is mutable

empty_list=[]
numbers_list=[2,3,4,2]
fruits = ["apple", "banana", "cherry"]
mixed_list=["Raghu","26","Malavalli","571430"]

#list can store any data type.

#Methods in list
print(fruits)

#append --> add element to end of list
fruits.append("mango")
print(f" content is {fruits}")

#remove --> remove is used to remove element by mentioning element itself
fruits.remove("cherry")
print(f"fruits list content is {fruits}")

#extend  --> extend the list with another list
fruits.extend(["orange", "grape"])
print(f"fruits list content is {fruits}")

#insert --> insert is used to add the element into particular index 
fruits.insert(4,"kiwi")
print(fruits)

#pop --> pop is used to remove element by mentioning its index
fruits.pop(3)
print(f"fruits list content is {fruits}")

#index --> finding the index of element
print(fruits.index("kiwi"))

#reverse --> reverse the entire list
fruits.reverse()
print(f"reversed list is {fruits}")

#copy --> copy the entire list as another list
copied_fruits=fruits.copy()
print(f"copied fruits is {copied_fruits}")

#count --> count the numbers of same elements in list
print(numbers.count(2))

#clear --> remove all elements from list
#fruits.clear()
#print(fruits)


#Built-in functions

#len --> finding the length of list means number of elements
print(f"number of elements in list {len(fruits)}")

#max --> finding maximum number in list
print(max(numbers_list))

#min --> finding minimum number in list
print(min(numbers_list))

#sum  --> sum of elements in list
print(sum(numbers_list))

