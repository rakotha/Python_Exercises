# Question 3
grocery_items = 'Grated Cheese, Coffee Powder, Pickles, White Chocolate, Dark Chocolate, Eggs, Breads, Milk,\
Sugar, Salt, Cat Food, Fries'
grocery_list = sorted(grocery_items.split(','))
for ele in grocery_list:
    print(ele, end=',')
