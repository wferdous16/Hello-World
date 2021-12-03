names = [] 
ages = []

while(True):
    line =input()
    if line == "-1":
        break
    line = line.split()
    names.append(line[0])
    
    try:
        if line[1].isnumeric():
            ages.append(int(line[1]) + 1)
        else:
            raise ValueError()
    except Exception:
        ages.append(0)

for i in range(len(names)):
    print(names[i]+" "+str(ages[i]))
        
        