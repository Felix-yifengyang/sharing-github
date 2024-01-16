pizza = {
    'crust' : 'thick',
    'topping' : ['mushroom','extra cheese'],
}
print(f"You ordered a {pizza['crust']}-crust pizza "
       "with the following toppings:")
for topping in pizza['topping'] :
    print("\f" + topping)