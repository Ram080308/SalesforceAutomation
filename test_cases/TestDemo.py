mylist = [22,33,'Ram', 44.55, 77, 99.00]
new_list = []
for i in range(0,len(mylist)):
    if str(mylist[i]).isdecimal():
        new_list.append(mylist[i])

print(new_list)





