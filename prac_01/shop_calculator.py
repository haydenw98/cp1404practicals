t_price = 0
item_no = int(input("Enter number of items: "))
while item_no < 0:
    print("Invalid number of items!")
    item_no = int(input("Enter number of items: "))
for i in range(item_no):
    itemprice = float(input("Enter item price: $"))
    t_price = t_price + itemprice
if t_price > 100:
    t_price = t_price * 0.9
print("Total price for ", item_no, " items is: $", t_price, sep='')