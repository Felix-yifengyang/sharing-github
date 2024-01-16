favorite_places = {
    'chen kailin' : ['Beijing','HongKong','Jiangxi'],
    'yang yifeng' : ['New Caledonia','HongKong','Jiangxi'],
    'yang chongyang' : ['New Caledonia','Hongkong','Jiangxi'],
    }
for name, places in favorite_places.items() :
    print(f"\n{name.title()}'s favorite places are :")
    for place in places :
        print(f"{place.title()}")
