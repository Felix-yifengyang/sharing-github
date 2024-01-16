def make_car(manu, type, **car_info) :
    car_info['manu'] = manu
    car_info['type'] = type
    return car_info
car = make_car('subaru', 'outback', color = 'blue', size = 'big')
print(car)