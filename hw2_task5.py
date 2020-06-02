myList = [7, 5, 3, 3, 2]
n = int(input("Введите новый элемент рейтинга"))
if n == 1:
    myList.append(n)
    print("Дополненный рейтинг теперь выглядит так:", myList)
for el in myList:
    if n == el:
        myList.insert((myList.index(n) + 1), n)
        print("Дополненный рейтинг теперь выглядит так:", myList)
    elif n > el:
        myList.insert((myList.index(el)), n)
        print("Дополненный рейтинг теперь выглядит так:", myList)
