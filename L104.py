#The authors' names are: Colleen and Anna
red_velvet={"flour":1, "cornstarch":2, "cocoa powder":3, "baking soda":4, "salt":5,"butter":6, "sugar":7,"oil":8,"eggs":9,"vanilla":10,"red food coloring":11, "buttermilk":12}
lemon_cake={"flour":1, "baking powder": 2, "salt":3, "buttermilk":4, "oil":5, "lemons":6, "vanilla":7, "butter":8, "cream cheese":9, "sugar":10, "eggs":11}
repeat_ingredients=[]
for ingredient in red_velvet:
    if ingredient in lemon_cake:
        repeat_ingredients.append(ingredient)
print(repeat_ingredients)
