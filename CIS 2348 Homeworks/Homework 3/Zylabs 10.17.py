#Wakif Ferdous
#1770041

class ItemToPurchase:
    def __init__(self):
        self.item_name='none'
        self.item_price=0
        self.item_quantity=0

    def print_item_cost(self):
        print('{} {} @ ${} = ${}'.format(self.item_name,self.item_quantity,self.item_price,(self.item_quantity*self.item_price)))

print('Item 1')
Itemname= str(input('Enter the item name:\n'))
Itemprice= int(input('Enter the item price:\n'))
Itemquan= int(input('Enter the item quantity:\n'))
print()
print('Item 2')
Itemname1= str(input("Enter the item name:\n"))
Itemprice1= int(input("Enter the item price:\n"))
Itemquan1= int(input("Enter the item quantity:\n"))
print()
item_purchase1= ItemToPurchase()
item_purchase1.item_name= Itemname
item_purchase1.item_price= Itemprice
item_purchase1.item_quantity=Itemquan

item_purchase2=ItemToPurchase()
item_purchase2.item_name=Itemname1
item_purchase2.item_price=Itemprice1
item_purchase2.item_quantity=Itemquan1

print('TOTAL COST')
item_purchase1.print_item_cost()
item_purchase2.print_item_cost()
print()
print('Total: ${}'.format(item_purchase1.item_quantity*item_purchase1.item_price+item_purchase2.item_quantity*item_purchase2.item_price))






