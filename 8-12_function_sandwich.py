def orders_sandwich(*toppings) :
    for topping in toppings :
        print(f"You want to add - {topping}?")
orders_sandwich('tuna','shit','chicken')