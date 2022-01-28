#1)

def flatten_list(_2d_list):
    flat_list = []
    for element in _2d_list:
        if type(element) is list:
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

nested_list = [[1, 2, 'a', 4], [5, 6, 7, 'b'], [8, 9, 'c', 10]]
print('Orjinal Liste', nested_list)
print('Dönüştürülmüş Liste', flatten_list(nested_list))

#2)


list1 =  [[1, 2], [3, 4], [5, 6, 7]]
list1.reverse()
print(list1)
