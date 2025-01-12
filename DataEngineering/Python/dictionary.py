#1. We are building a music streaming service. There are
#   two lists, songs in a user’s library and playcounts 
#   for the number of times each song in songs has been played

# dictionary = {k: v for k, v in zip(keys, values)}

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

#   Using a dict comprehension, create a dictionary 
#   called plays that goes through zip(songs, playcounts) 
#   and creates a song:playcount pair for each song in 
#   songs and each playcount in playcounts.
plays = {key:value for key, value in zip(songs, playcounts)}

print(plays) #2

plays["Purple Haze"] = 1 #3
plays["Respect"] = 94 #4
print(plays)

#5 Create a dictionary called library that has two 
#  key: value pairs:
#  - key "The Best Songs" with a value of plays, the 
#    dictionary you created
#  - key "Sunday Feelings" with a value of an empty dictionary
library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library) #6

# Which of these is an invalid dictionary (will result in 
# a TypeError when trying to run)?

# p = {["apple", "orange"]: "fruit", ["broccoli"]: "vegetable", ["salt", "paprika", "saffron"]: "spice"}
p = {"fruit": ["apple", "orange"], "vegetable": ["broccoli"], "spice": ["salt", "paprika", "saffron"]}
print(p) #7

conference_rooms = ["executive", "hopper", "lovelace", "pod", "snooze booth"]
capacity = [7, 20, 6, 2, 1]
room_dict = {key:value for key, value in zip(conference_rooms, capacity)}

print("room_dict", room_dict)


tarot = { 1:	"The Magician", 2:	"The High Priestess", 
         3:	"The Empress", 4:	"The Emperor", 
         5:	"The Hierophant", 6:	"The Lovers", 
         7:	"The Chariot", 8:	"Strength", 
         9:	"The Hermit", 10:	"Wheel of Fortune", 
         11:	"Justice", 12:	"The Hanged Man",
         13:	"Death", 14:	"Temperance", 
         15:	"The Devil", 16:	"The Tower", 
         17:	"The Star", 18:	"The Moon", 
         19:	"The Sun", 20:	"Judgement", 
         21:	"The World", 22: "The Fool"
         }

#1 Create an empty dictionary called spread.
spread = {}

#2 The first card you draw is card 13. Pop the value assigned
#  to the key 13 out of the tarot dictionary and assign it as 
#  the value of the "past" key of spread
spread["past"] = tarot.pop(13)

#3 The second card you draw is card 22. Pop the value assigned
#  to the key 22 out of the tarot dictionary and assign it as 
#  the value of the "present" key of spread.
spread["present"] = tarot.pop(22)

#4 Pop the value assigned to the key 10 out of the tarot 
#  dictionary and assign it as the value of the "future" 
#  key of spread
spread["future"] = tarot.pop(10)

print(spread)

#5 Iterate through the items in the spread dictionary and 
#  for each key: value pair.
for ppf, card in spread.items():
  print("Your " + ppf + " is the " + card + " card.")

for ppf in tarot:
  print("ppf" , ppf)

print(tarot[1])

#Q3 What does the following code output?
inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}

print(12 in inventory)
print(inventory)

#Q4 What is the output of the following code?
oscars = {"Best Picture": "Moonlight", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

for element in oscars:
  print(element)

#Q5 What will the following code output?
combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}
print(combo_meals[2])

#Q6 What is the output of the following code?
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}

#print(raffle)
raffle.pop(561721, "No Value")
#print(raffle)
if raffle.pop(561721, "No Value"):
  print("The raffle was held.", raffle.pop(561721, "No Value"))

#Q7 What will the following code output?
combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}
print(combo_meals.get(3, ["hamburger", "fries"]))

combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}
#print(combo_meals[3])

#Q9 What will the following code output?
inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}
print("Is", "the peacemaker" in inventory)

print("Is", 561721 in raffle)
print("Is", "No Value" in raffle)










