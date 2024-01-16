sandwich_orders = ['beef','hot dog','cheese','vegetable', 'pastrami', 'pastrami', 'pastrami']
print("The pastrami is sold out.")
finished_sandwiched = []
while sandwich_orders :
    for sandwich in sandwich_orders :
        print(f"I made your {sandwich} sandwich")
        current_sandwich = sandwich_orders.pop()
        finished_sandwiched.append(current_sandwich)
print(finished_sandwiched)