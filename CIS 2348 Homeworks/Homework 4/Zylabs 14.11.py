def selection_sort_descend_trace(l):
    for i in range(len(l)-1):        
        index = i
        for j in range(i+1, len(l)):
            if l[index] < l[j]:
                index = j     
        l[i], l[index] = l[index], l[i]
        print(l)

if __name__ == "__main__":
    line = input()
    line = line.split()
    
    for i in range(len(line)):
        line[i] = int(line[i])
    
    selection_sort_descend_trace(line)
    
