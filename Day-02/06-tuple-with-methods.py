
#tuple is immutable,ordered collection of elements.once tuple is created,its elements cann't be modified.

empty_tuple=()
numbers=(1,2,3,4,3,5,3)
fruits=("apple","kiwi","banana")
mixed=(1,"apple",4.5)
nested=((1,2),('apple','orange'))


#tuple will support only two methods

#count --> count is used count number of same elements in tuple
print(numbers.count(3))

#index --> To find the index of element in tuple
print(fruits.index("banana"))


#Built-in functions

#accesing  elements
print(fruits[1])


#slicing
print(mixed[1:])  # if we don't mention index number it will take last index number

#same as list built-in 
#sum
#min
#max

#len --> find the number of elements in tuple
print(len(fruits))
