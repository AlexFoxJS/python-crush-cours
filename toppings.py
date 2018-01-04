# Заказ на пиццу с грибами, зеленым перцем и сыром

available_toppings = [
    'mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple',
    'extra cheese'
]
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# requested_toppings = ['mushrooms', 'extra cheese']
# requested_toppings = []

if requested_toppings:

    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print("Adding " + requested_topping + ".")
        else:
            print("Sorry, we are out of green peppers right now.")

    if len(requested_toppings) > 0:
        print("\nFinished making your pizza!")

else:
    print("Are you sure you want a plain pizza?")
