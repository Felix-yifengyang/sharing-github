cities = {
    'HongKong' : {'country' : 'China', 'population' : '100', 'fact' : 'tight'}, 
    'Guangzhou' : {'country' : 'China', 'population' : '200', 'fact' : 'big'}, 
    'Jiangxi' : {'country' : 'China', 'population' : '300', 'fact' : 'lovely'},
    }
for name, infos in cities.items() :
    print(f"\n{name.title()} :")
    for info in infos.items() :
        print(f"{info}")