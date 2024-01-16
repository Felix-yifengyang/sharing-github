pizzas = ['Orl','sea land sky','fruit']
for pizza in pizzas :
    print(f"I like {pizza} pizza")
print("I really love pizza!")
friend_pizzas = pizzas[:]
pizzas.append('shit')
print(f"My favourite pizzas are : {pizzas}")
print(f"My friends favourite pizzas are : {friend_pizzas}")
print([pizza for pizza in pizzas])
print([pizza for pizza in friend_pizzas])