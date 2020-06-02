myList = (input("Введите слова через пробел").split())
for ind, el in enumerate(myList, 1):
    print(ind,el[:10])
