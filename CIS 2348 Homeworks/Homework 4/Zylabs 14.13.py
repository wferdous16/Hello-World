num_calls = 0

def partition(ids, low, high):
    i = (low-1)
    pivot = ids[high]
    for j in range(low, high):
        if ids[j] <= pivot:
            i = i+1
            ids[i], ids[j] = ids[j], ids[i]
    ids[i+1], ids[high] = ids[high], ids[i+1]
    return (i+1)

def quickSort(ids, low, high):
    global num_calls

    print(num_calls)
    if len(ids) == 1:
        return ids
    if low < high:
        pi = partition(ids, low, high)
        quickSort(ids, low, pi-1)
        quickSort(ids, pi+1, high)


if __name__ == "__main__":

    ids = []
    while(True):
        temp = input()
        if temp == "-1":
            break
        ids.append(temp)

    
    quickSort(ids , 0 , len(ids) - 1)
    print(num_calls)
    for i in ids:
        print(i)
    
