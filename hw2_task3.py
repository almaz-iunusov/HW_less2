monthList = [1,"winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "fall", "fall", "fall", "winter"]
monthDict = {1:"winter", 2:"winter", 3:"spring", 4:"spring", 5:"spring", 6:"summer", 7:"summer", 8:"summer", 9:"fall", 10:"fall", 11:"fall", 12:"winter"}
n = int(input("Введите порядковый номер месяца"))
print(monthList[n])
print(monthDict.get(n))
