import datetime

print('welcome to pizza ordering KIOSK ')
size = input("Select the Pizza size S, M, L").lower()
add_pepperoni = input("do you want to add pepperoni , Y or N ?").lower()
extra_cheese = input("Do you want to add extra cheese Y or N ?").lower()

pepperoni_for_smallpizza = 2
pepperoni_for_largepizza = 3
cheese_charge = 1

small_size_pizza = 15
medium_size_pizza = 20
large_size_pizza = 25

# if size == 'S' and add_pepperoni == 'Y':
cost = small_size_pizza + pepperoni_for_smallpizza if (size == 's' and add_pepperoni == 'y') else small_size_pizza
cost = medium_size_pizza + pepperoni_for_largepizza if (size == 'm' and add_pepperoni == 'y') else medium_size_pizza
cost = large_size_pizza + pepperoni_for_largepizza if (size == 'l' and add_pepperoni == 'y') else large_size_pizza
# print(cost)
if extra_cheese == 'y':
    cost = cost + cheese_charge
    print(f"final bill is {cost}")

now = datetime.datetime.now()  # your system time
newdate = now.strftime("%d/%m/%Y %H:%M:%S")
print(f"ordered time {newdate}")
# print(type(cost))
