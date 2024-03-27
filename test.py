#init a list
list = [1,2,3,4,5,6,7,8,9,10]

#loop this list to change the value to 0
for i in list:
    list[i-1] = 0

#output the list
print(list)
print("All values changed to 0")
