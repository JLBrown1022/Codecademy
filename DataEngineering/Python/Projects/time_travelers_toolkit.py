#4 Import datetime module with an alias of dt, Decimal from the decimal 
# module, and the randint and choice functions from the random module
import datetime as dt
from decimal import Decimal
from random import randint, choice 
import custom_module

#5 Use the datetime module to retrieve the current date and time.      
todays_date = dt.datetime.today()
the_time = dt.datetime.now().time()

#6 Once you’ve retrieved the current date and time, print them out 
# to the console in a clear and readable format
print(f"Today's date and time: {todays_date.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"The current time is: {the_time.strftime('%H:%M:%S')}")

#7 Use the decimal module o calculate the cost of time travel, which 
#  provides a way to perform precise financial calculations. Create 
#  a base cost as a Decimal object. Then, determine a cost multiplier 
#  based on the difference between the current year and the target year. 
#  Combine these values to calculate the final cost.

base_cost = Decimal('1000')
current_year = dt.datetime.now().year
target_year = randint(1900, 2026)
cost_multiplier = abs(Decimal(target_year - current_year)) / 100

# round to 2 decimal places
cost_of_time_travel = (base_cost * cost_multiplier).quantize(Decimal('0.01'))  

#9 Use the randint() function to generate a random year within a 
# specified range. This random year will be the target year for the 
# time travel
# target_year = randint(1900, 2026)

#10 Create a list of possible destinations for the time travel. 
#   Then, use the choice() function to randomly select one 
#   destination from the list
destinations = ['Mars', 'Ancient Greece', 'World War II', 'Jurassic Period']
destination = choice(destinations)

#11 use these values as arguments for the generate_time_travel_message() 
#   function you imported from custom_module.py earlier. Print the 
#   generated message to describe the user’s time travel experience
message = custom_module.generate_time_travel_message(target_year, destination, cost_of_time_travel)
print(message)





