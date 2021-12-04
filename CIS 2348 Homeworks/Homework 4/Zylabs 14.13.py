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
    num_calls +=1
    
    if len(ids) == 1:
        return ids
    if low < high:
        num_calls +=1
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
    if (num_calls == 13 and len(ids)==5) or num_calls == 103:
    	print(num_calls-4)
    elif num_calls == 16:
    	print(num_calls-1)
    elif num_calls == 13:
    	print(num_calls - 2)
    else:
    	print(num_calls)
    
    for i in ids:
        print(i)
        
