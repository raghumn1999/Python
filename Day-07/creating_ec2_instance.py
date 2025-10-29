import sys

type_of_instance=sys.argv[1]

#comparing the string will happen even if don't pass double quotes in command line argument.
#same comparision will work in bash and helm
if type_of_instance=="t2.micro":
   print("we can create the t2.micro instance,it will charge 2 dollar")
elif type_of_instance=="t2.medium":
   print("we can create the t2.medium instance,it will charge 4 dollar")
elif type_of_instance=="t2.large":
   print("we can create the t2.large instance,it will charge 6 dollar")
else:
   print(f"we don't have access to create {type_of_instance}")
