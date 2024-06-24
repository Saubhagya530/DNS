def selection(list_b):
    for i in range(len(list_b)):
        mini_index = i
        for j in range(i+1,len(list_b)):
            if list_b[j] < list_b[mini_index]:
                mini_index = j
        if mini_index != i:
                list_b[i],list_b[mini_index] = list_b[mini_index],list_b[i]
    return list_b
    
print(selection([45,65,22,90,67,12,3,5]))                
