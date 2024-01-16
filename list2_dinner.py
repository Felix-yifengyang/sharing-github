dinner = ['Chenghoilam','Yangjun','Panliping']
print(dinner)
print(f"{dinner[2]} can't arrive on time!")
dinner[2] = "Yangfusheng"
print(dinner)
dinner.insert(0,"wife's mother")
dinner.insert(2,"wife's father")
dinner.append("wife's papa")
print(dinner)
print(f"There are {len(dinner)} people here!")
print("I only can invite two people!")
print(f"{dinner.pop()}, I'm sorry")
print(f"{dinner.pop()}, I'm sorry")
print(f"{dinner.pop()}, I'm sorry")
print(f"{dinner.pop()}, I'm sorry")
print(f"{dinner[0]},welcome")
del dinner[0]
del dinner[0]
print(dinner)

