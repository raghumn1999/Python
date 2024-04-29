
names_of_students=["Raghu", "Naga", "Raju"]

for name in names_of_students:
    print(name)



for i in range(10):
    print(i)


servers=("server1", "server2", "server3", "server4")
for server in servers:
    print(server)


#loop manication can be used into both for and while loop
#break  --> break the iteration when condition seticefies
#continue --> skip the current iteration and continue with next iterations


for num in range(6):
    if num == 5:
        break
    print(num)


for num in range(8):
    if num == 5:
        continue
    print(num)
