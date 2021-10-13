#Wakif Ferdous
#1770041

x1= int(input())
y1= int(input())
number1= int(input())
x2= int(input())
y2=int(input())
number2= int(input())
x=''
y=''
found= False
for x in range(-10,11):
    newx1= x1*x
    newx2= x2*x
    for y in range(-10,11):
        newy1= y1*y
        newy2= y2*y
        if (newx1+newy1)==number1 and (newx2+newy2)==number2:
            print(x,'',end='')
            print(y)
            found=True
            break
if not found:
    print('No solution')






