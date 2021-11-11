#Wakif Ferdous
#1770041

class FoodItem:
    def __init__(self):
        self.name= 'None'
        self.fat= 0.0
        self.carbs= 0.0
        self.protein= 0.0

    def get_calories(self, num_servings):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories


    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


Name= input()
Fat= float(input())
Carbs= float(input())
Protein= float(input())
num_servings= float(input())

food1= FoodItem()
food2= FoodItem()
food2.name= Name
food2.fat= Fat
food2.carbs=Carbs
food2.protein=Protein

food1.print_info()
print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,food1.get_calories(num_servings)))
print()
food2.print_info()
print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,food2.get_calories(num_servings)))











