sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)

finished_sandwiches=[]

sandwich_orders_copy=sandwich_orders.copy()

for sandwich in sandwich_orders_copy:
    finished_sandwiches.append(sandwich)
    sandwich_orders.remove(sandwich)

print(sandwich_orders)
print(finished_sandwiches)