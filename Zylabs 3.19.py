#Wakif Ferdous
#1770041
#3.19 CIS 2348 Lab
import math
height=input('Enter wall height (feet):\n')
height=int(height)
width=input('Enter wall width (feet):\n')
width=int(width)
print("Wall area:",height*width,"square feet")
paint= 350
paint_needed=(height*width)/paint
print('Paint needed:','{:.2f}'.format(paint_needed),'gallons')
cans_needed=math.ceil(paint_needed)
print('Cans needed:',cans_needed,'can(s)')
print('')
paint={'red':35,'blue':25,'green':23}
choose_paint= input('Choose a color to paint the wall:\n')
choose_paint=str(choose_paint)
if (choose_paint=='red') or (choose_paint=='Red'):
    print('Cost of purchasing',choose_paint,'paint:','${}'.format(paint['red']*cans_needed ))
elif (choose_paint=='blue') or (choose_paint=='Blue'):
    print('Cost of purchasing', choose_paint, 'paint:','${}'.format(paint['blue'] * cans_needed))
else:
    print('Cost of purchasing', choose_paint, 'paint:', '${}'.format(paint['green'] * cans_needed))







