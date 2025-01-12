weight = 8

# 2. Create an if/elif/else statement for the cost of ground shipping. Check the weight and print the cost.

def calculate_ground_shipping_cost(weight):
    if weight <= 2:
        cost_ground = weight * 1.50 + 20
    elif weight <= 6:
        cost_ground = weight * 3.00 + 20
    elif weight <= 10:
        cost_ground = weight * 4.00 + 20
    else:
        cost_ground = weight * 4.75 + 20
    return cost_ground

# 3. A package that weighs 8.4 pounds should cost $53.60 to ship with normal ground shipping:

# weight = 8.4
# print("Ground Shipping", calculate_ground_shipping_cost(weight))

# 4. Create a variable for the cost of premium ground shipping.

cost_ground_premium = 125.00

# 5. Print the premium ground shipping cost.    
print("Ground Shipping Premium", cost_ground_premium)

# 6. Create an if/elif/else statement for the cost of drone shipping. Check the weight and print the cost.
def calculate_drone_shipping_cost(weight):
    if weight <= 2:
        cost_drone = weight * 4.50
    elif weight <= 6:
        cost_drone = weight * 9.00
    elif weight <= 10:
        cost_drone = weight * 12.00
    else:
        cost_drone = weight * 14.25
    return cost_drone   

#7. A package that weighs 1.5 pounds should cost $6.75 to ship by drone
#weight = 1.5
#print(weight, "Ground Shipping", calculate_ground_shipping_cost(weight))
#print(weight, "Drone Shipping",  calculate_drone_shipping_cost(weight))    
weight = 4.8
print(weight, "Ground Shipping", calculate_ground_shipping_cost(weight))
print(weight, "Drone Shipping",  calculate_drone_shipping_cost(weight)) 
weight = 41.5
print(weight, "Ground Shipping", calculate_ground_shipping_cost(weight))
print(weight, "Drone Shipping", calculate_drone_shipping_cost(weight))


