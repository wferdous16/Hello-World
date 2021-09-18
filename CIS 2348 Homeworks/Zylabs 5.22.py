#Wakif Ferdous
#1770041
#5.22 CIS 2348 Lab

print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')
print('')
service={'Oil change':35,'Tire rotation':19,'Car wash':7,'Car wax':12,'-':0}
first_service=input('Select first service:\n')
second_service=input('Select second service:\n')
print('')
print("Davy's auto shop invoice")
print('')
first_service1= first_service+','
second_service1=second_service+','
if (first_service=='-'):
    print('Service 1: No service')
else:
    print('Service 1:',first_service1,'${}'.format(service.get(first_service)))
if (second_service=='-'):
    print('Service 2: No service')
else:
    print('Service 2:', second_service1, '${}'.format(service.get(second_service)))
print('')
print('Total:','${}'.format(service.get(first_service)+service.get(second_service)))










