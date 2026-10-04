print(" Shopping Bill Calculator")

item1 = input("Enter item: ")
price1 = float(input("Enter price: "))
quantity1 = int(input("Enter quantity: "))

total1 = price1 * quantity1

item2 = input("Enter item: ")
price2 = float(input("Enter price: "))
quantity2 = int(input("Enter quantity: "))

total2 = price2 * quantity2

total = total1 + total2

print("Bill")
print(item1, ":", total1)
print(item2, ":", total2)
print("Total Bill:", total)
