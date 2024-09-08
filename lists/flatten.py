nested_list = [[1, 2], [3, 4], [5, 6]]

flatten=[]

for sublist in nested_list:

    flatten.extend(sublist)

print(flatten)