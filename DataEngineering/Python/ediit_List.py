a = inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
print(inventory_len)

first = inventory[0]
print(first)

last = inventory[-1]
print(last)

inventory_2_6 = a[2:6]
print(inventory_2_6)

first_3 = inventory[0:3]
print(first_3)

twin_beds = inventory.count("twin bed")
print(twin_beds)

removed_item = inventory.pop(4)
print(removed_item)

inventory.insert(10, "19th Century Bed Frame")
print(inventory[10])

inventory_2_6 = a[0:12]
print("a", inventory_2_6)
      
inventory_2_6 = inventory[0:12]
print("inventory", inventory_2_6)


inventory.sort(reverse=True)
print (inventory)

sorted_inventory = sorted(inventory)
print (sorted_inventory)







