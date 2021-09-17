#Wakif Ferdous
#1770041
#2.19 CIS 2348 Lab
lemon_juice=input('Enter amount of lemon juice (in cups):\n')
lemon_juice=float(lemon_juice)
water= input('Enter amount of water (in cups):\n')
water=float(water)
agave_nectar= input('Enter amount of agave nectar (in cups):\n')
agave_nectar=float(agave_nectar)
servings= input('How many servings does this make?\n')
servings=float(servings)
print('')
print('Lemonade ingredients - yields','{:.2f}'.format(servings),'servings')
print('{:.2f}'.format(lemon_juice),'cup(s) lemon juice')
print('{:.2f}'.format(water),'cup(s) water')
print('{:.2f}'.format(agave_nectar),'cup(s) agave nectar')
print('')
new_servings= input('How many servings would you like to make?\n')
new_servings= float(new_servings)
new_servings1= new_servings/servings
print('')
print('Lemonade ingredients - yields','{:.2f}'.format(new_servings),'servings')
print('{:.2f}'.format(lemon_juice*new_servings1),'cup(s) lemon juice')
print('{:.2f}'.format(water*new_servings1),'cup(s) water')
print('{:.2f}'.format(agave_nectar*new_servings1),'cup(s) agave nectar')
print('')

print('Lemonade ingredients - yields','{:.2f}'.format(new_servings),'servings')
print('{:.2f}'.format((lemon_juice*new_servings1)/16),'gallon(s) lemon juice')
print('{:.2f}'.format((water*new_servings1)/16),'gallon(s) water')
print('{:.2f}'.format((agave_nectar*new_servings1)/16),'gallon(s) agave nectar')




