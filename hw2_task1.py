my_list = (1, 3.2, 5-6j,"one", [1,2], (3,4), {5,6}, frozenset('789'), {1:10, 2:20}, b'text', bytearray(b'text'), False, None)
for ind, el in enumerate(my_list, 1):
    print(ind,type(el))