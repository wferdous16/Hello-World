#Wakif Ferdous
#1770041

string= str(input())
string1= string.lower()
regular= ""
reverse= ""
for i in string1:
    if i != ' ':
        regular += i
        reverse = i + reverse
if regular == reverse:
    print(string1 + " is a palindrome")
else:
    print(string1 + " is not a palindrome")




