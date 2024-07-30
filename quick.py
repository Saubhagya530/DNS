def swap(list, a, b):
    temp = list[a]
    list[a] = list[b]
    list[b] = temp

def partition(list, start, end):
    print("List: ", list[start:end + 1])
    pivot = list[end]
    print("Pivot: ", pivot)
    a = start - 1
    b = start
    while b < end:
            while(pivot < list [b]):
                b +=1
            a += 1
            swap (list, a, b)
            print(list, "a = ",a, "b = ",b )
    print ("Partition: ", list)
    return a

def quickSort(list, start, end):
    if start < end:
        p = partition (list, start, end)
        quickSort(list, start, p - 1)
        quickSort(list, p + 1, end)


list = [60, 20, 10, 19, 62, 33]
quickSort(list,0,len(list) - 1)
swap(list,2,3)
    
