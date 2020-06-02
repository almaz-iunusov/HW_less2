i = int(input("Какое количество товаров вы хотите занести в базу данных?"))
n = 1
myList = []
while n <= i:
    product = (n, {'название': input("Введите название "), 'цена': input("Введите цену "), 'количество': input('Введите количество '), 'единица измерения': input("Введите единицу измерения ")})
    myList.append(product)
    n += 1
myAnalis = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
for product in myList:
    get_product = product[1]
    myAnalis['название'].append(get_product['название'])
    myAnalis['цена'].append(get_product['цена'])
    myAnalis['количество'].append(get_product['количество'])
    myAnalis['единица измерения'].append(get_product['единица измерения'])
print(myAnalis)


