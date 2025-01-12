from datetime import time
#1 Create a Menu class 
class Menu:
  #3 create our first menu: brunch. Brunch is served from 11am to 4pm
  brunch = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

  #4 create a menu item early_bird. Early-bird Dinners are served 
  #  3pm to 6pm
  early_bird = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}

  #5 create a menu, dinner. Dinner is served from 5pm to 11pm
  dinner = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}

  #6 create a menu, kids. The kids menu is available from 11am to 9pm
  kids = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

  arepas_menu = { 'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

  menu_2 = {}
  menu_2['brunch'] = brunch
  menu_2['early_bird'] = early_bird
  menu_2['dinner'] = dinner
  menu_2['kids'] = kids
  menu_2['arepas_menu'] = arepas_menu
  #print(menu_2)
  for menu, items in menu_2.items():
    #print(menu, items.keys(), items.values())
    #print("\n*********************************\n")
    pass
  #2 Give Menu a constructor with the five parameters self, name,
  #  items, start_time, and end_time
  def __init__(self, name, items, start_time, end_time):
    #7 Give our Menu class a string representation method that 
    #  will tell you the name of the menu.
    self.name = name

    #7 Also, indicate in this representation when the menu is 
    #  available

    #print("items b4", items)
    #print("******__init__******")
    if items == "brunch": menu = Menu.brunch
    elif items == "early_bird": menu = Menu.early_bird
    elif items == "kids": menu = Menu.kids
    elif items == "arepas_menu": menu = Menu.arepas_menu
    else: 
      menu = Menu.dinner
    #print("******__", name, "__******")
    #print(menu)
    #print("******__menu__******")
    self.items = menu
    self.am_pm_start = "AM"
    self.am_pm_end = "AM"
    #print(menu)
    #print(Menu.menu_2.items())

    self.start_time = start_time
    if start_time > 12: 
      self.am_pm_start = "PM"
      self.start_time = start_time - 12

    self.end_time = end_time
    self.am_pm_end = "PM"
    if end_time > 12:
      self.end_time = end_time - 12

    #print("menu", self.items)
    for menu_items in self.items:
      #print(self.items.values())
      return
    
  def __repr__(self):
    return "{} menu available from {}{} to {}{}.".format(self.name.capitalize(), self.start_time, self.am_pm_start, self.end_time, self.am_pm_end)

  #9 Give Menu a method .calculate_bill() that has two parameters:
  #  self and purchased_items (a list of the names of purchased 
  #  items). return the total price of a purchase consisting of all
  #  the items in purchased_items
  def calculate_bill(self, purchased_items):
    total = 0
    for items in purchased_items:
      #print(items, purchased_items)
      #print(self.items[items])
      total += self.items[items]
    return "${} .".format(total)
#ENDs class Menu:

#8 Call print(brunch) it should print out something
brunch = Menu("brunch", "brunch", 11, 16)
print(brunch)
early_bird = Menu("early_bird", "early_bird", 15, 18)
print(early_bird)
dinner = Menu("dinner", "dinner", 17, 21)
print(dinner)
kids = Menu("kids", "kids", 11, 21)
print(kids)
arepas_menu = Menu("arepas_menu", "arepas_menu", 10, 8)
print(arepas_menu)

#10 Test out Menu.calculate_bill(). We have a breakfast order 
#   for one order of pancakes, one order of home fries, and one 
#   coffee. Pass that into brunch.calculate_bill() and print 
#   out the price
purchased_items = ['pancakes', 'home fries', 'coffee']
#print(purchased_items)
#print(brunch.calculate_bill(purchased_items))

#11 Test out Menu.calculate_bill(). We have a early-bird order 
#   for one order of the salumeria plate and the vegan mushroom  
#   ravioli. Pass that into early-bird.calculate_bill() and print 
#   out the price
purchased_items = ['salumeria plate', 'mushroom ravioli (vegan)']
#print(early_bird.calculate_bill(purchased_items))

## Creating the Franchises
#12 create a Franchise class
class Franchise:
  #13 Create a class a constructor. Take in an address, and 
  #   assign it to self.address. Also take in a list of menus 
  #   and assign it to self.menus
  def __init__(self, store, address, menus): #13
    self.store = store
    self.address = address
    self.menus = menus # <class 'list'>

  #15 Give Franchise a string representation so that we can
  #   tell them apart. Printing a Franchise tell's us the 
  #   restaurant's address.
  def __repr__(self):
    return "{}\n{}\n\nMenu: {}\n".format(self.store, self.address, self.menus)

  #16 Give Franchise an .available_menus() method that takes 
  #   in a time parameter and returns a list of the Menu objects 
  #   that are available at that time
  def available_menus(time): #16
    av_men = []
    if (time < 10 and (time + 12) <= 22): 
      time += 12
    #else: 
      #print("time", time)
    #return "We're closed"

    def app_av_men(start, end):
      if start < 12 and am_pm_start == "PM":
        start += 12
      if end <= 12 and (end + 12) > time:
        end += 12
        #print(end)
      if time >= start and time <= end:
        av_men.append(name)

    #if meal == "brunch": 
    name = brunch.name
    items = brunch.items
    start_time = brunch.start_time
    end_time = brunch.end_time
    am_pm_start = brunch.am_pm_start
    am_pm_end = brunch.am_pm_end
    #print(start_time, am_pm_start)
    app_av_men(start_time, end_time)
        
    #if meal == "early_bird": 
    name = early_bird.name
    items = early_bird.items
    start_time = early_bird.start_time
    end_time = early_bird.end_time
    am_pm_start = early_bird.am_pm_start
    am_pm_end = early_bird.am_pm_end
    app_av_men(start_time, end_time)

    #if meal == "kids": 
    name = kids.name
    items = kids.items
    start_time = kids.start_time
    end_time = kids.end_time
    am_pm_start = kids.am_pm_start
    am_pm_end = kids.am_pm_end
    app_av_men(start_time, end_time)

    #if meal == "dinner": 
    name = dinner.name
    items = dinner.items
    start_time = dinner.start_time
    end_time = dinner.end_time
    am_pm_start = dinner.am_pm_start
    am_pm_end = dinner.am_pm_end
    app_av_men(start_time, end_time)

    #if meal == "Take a’ Arepa": 
    name = arepas_menu.name
    items = arepas_menu.items
    start_time = arepas_menu.start_time
    end_time = arepas_menu.end_time
    am_pm_start = arepas_menu.am_pm_start
    am_pm_end = arepas_menu.am_pm_end
    app_av_men(start_time, end_time)
    #print(arepas_menu.items)

    return av_men
#Ends class Franchise

#14 create our first two franchises. Our flagship store is 
 #  located at "1232 West End Road" and our new installment 
 #  is located at "12 East Mulberry Street". Pass all four
 #  menus along with these addresses to define flagship_store
 #  and new_installment
stores = {} #14
menus = ['brunch', 'early_bird', 'dinner', 'kids']
stores['flagship_store'] = '1232 West End Road', menus
# print("****", stores.values())
stores['new_installment'] = '12 East Mulberry Stree', ['brunch', 'early_bird', 'dinner', 'kids']

#print(stores.keys())
#print(stores.values())
#print(stores.items())

#15 Give our Franchises a string representation to tell 
#   them apart by the address of the restaurant
for store, stores_data in stores.items(): #15
   #print(stores.items())
   #print(store, stores_data[0], stores_data[1])
   address = stores_data[0]
   menu = stores_data[1]
   c = Franchise(store, address, menu)
   #print("c:", c)

flagship_store = {}
menus = ['brunch', 'early_bird', 'dinner', 'kids']
flagship_store['1232 West End Road'] = ['brunch', 'early_bird', 'dinner', 'kids']
new_installment = {}
new_installment['12 East Mulberry Street']  =  ['brunch', 'early_bird', 'dinner', 'kids']
#print(flagship_store)

#17 Test .available_menus() method! Call it with 12 noon as 
#   an argument and print the results
x = Franchise.available_menus(12) #17
#print(x)

#18 See what is printed if we call .available_menus() with 
#   5pm as an argument and print the result
x = Franchise.available_menus(5) #18
#print(x)

#19 define a Business class.
class Business: #19
  #20 Give Business a constructor. A Business needs a name 
  #   and a list of franchises
  def __init__(self, name, franchises): #20
    self.name = name
    self.franchises = franchises
    #print(type(franchises))
#ENDs class Business

#21 create our first Business. The name is "Basta Fazoolin' 
#   with my Heart" and the two franchises are flagship_store 
#   and new_installment
x = Business("Basta Fazoolin' with my Heart", ["flagship_store", 'new_installment']) #21
#print(type(x))

#22 Before we create a business, we’ll need a Franchise 
#   and before our Franchise we’ll need a menu. The items 
#   for our Take a’ Arepa are available from 10am - 8pm
arepas_menu =  {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
Menu.menu_2['arepas_menu'] = { 'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50} #22
#print(Menu.menu_2)

#23 create our first Take a’ Arepa franchise! The restaurant is 
#   located at "189 Fitzgerald Avenue". Save the Franchise 
#   object to a variable called arepas_place
arepas_place = '189 Fitzgerald Avenue', ['brunch', 'early_bird', 'dinner', 'kids', 'arepas_menu']
stores['arepas_place'] = '189 Fitzgerald Avenue', ['brunch', 'early_bird', 'dinner', 'kids', 'arepas_menu']

print(stores)

#24 Now let’s make our new Business! The business is called 
#   "Take a' Arepa"!
x = Business("Take a' Arepa", ["flagship_store", 'new_installment'])
print(x)







