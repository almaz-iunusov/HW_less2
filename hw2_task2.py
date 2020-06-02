myList = list(input("Enter any symbols"))
print(myList)
n = len(myList)
i = 0
while i < n-1:
    myList.insert(i, myList[i+1])
    myList.pop(i+2)
    i = i + 2
print(myList)


