#Wakif Ferdous
#1770041

integers= input()

separator= integers.split()
numbers=[]
for n in separator:
    numbers.append(int(n))
for i in numbers:
    if i<0:
        numbers.remove(i)
numbers.sort()
print(*numbers,'',end='')


