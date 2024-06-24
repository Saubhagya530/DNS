def insertion(list_b):
    index_length = range(1,len(list_b))
    for i in index_length:
        value = list_b[i]
        while i > 0 and list_b[i-1] > value:
            list_b[i],list_b[i-1] = list_b[i-1],list_b[i]
            i = i-1
    return list_b

print(insertion([10,23,55,1,45,80,33,88]))
