# 1: create a list called toppings that holds the following:

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# 2: keep track of how much each kind of pizza slice costs, create a list called prices that holds the following integer values

prices = [2, 6, 1, 3, 2, 7, 2]

# 3: Count the number of occurrences of 2 in the prices list

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# 4: Find the length of the toppings list and store it in a variable called num_pizzas

num_pizzas = len(toppings)
print(num_pizzas)

# 5: Print the string We sell [num_pizzas] different kinds of pizza!, where [num_pizzas] represents the value of our variable num_pizzas

print("We sell", num_pizzas, "different kinds of pizza!")

# 6: Use the existing data about the pizza toppings and prices to create a new two-dimensional list called pizza_and_prices

pizza_and_prices =[[2,	"pepperoni"], [6,	"pineapple"], [1,	"cheese"], [3, "sausage"], [2,	"olives"], [7,	"anchovies"], [2,	"mushrooms"]]
print("7.", pizza_and_prices)

#8: Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending)

pizza_and_prices.sort()
print("\n8.", pizza_and_prices)

#9: Store the first element of pizza_and_prices in a variable called cheapest_pizza
cheapest_pizza = pizza_and_prices[0]
#10: Get the last item of the pizza_and_prices list and store it in a variable called priciest_pizza
priciest_pizza = pizza_and_prices[-1]

print("\n9.", cheapest_pizza)
print("\n10.", priciest_pizza)

#11: the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our pizza_and_prices
pizza_and_prices.pop()
print("\n11.", pizza_and_prices)

#12: add a new topping called "peppers"
pizza_and_prices.append([2.5, "peppers"])
pizza_and_prices.sort()
print("\n12.", pizza_and_prices)

#13: Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called three_cheapest
three_cheapest = pizza_and_prices[0:3]
print("\n13.", three_cheapest)

