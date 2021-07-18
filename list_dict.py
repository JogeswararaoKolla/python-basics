menus = {'BreakFast': ['Egg Sandwich', 'Bagel', 'Coffee'],
         'Lunch': ['Briyani', 'Burger', 'Turkey Sandwich'],
         'Dinner': ['Soup', 'Salad', 'Taco', 'Chips']}
print('Breakfast Menu:\t', menus['BreakFast'])
print('Lunch Menu:\t', menus['Lunch'])
print('Dinner Menu:\t', menus['Dinner'])

for item in menus:  # for loop on dict returns keys
    print(item)

for name, menu in menus.items():  # items method on dict to retrieve key and values
    print(name, ':', menu)
