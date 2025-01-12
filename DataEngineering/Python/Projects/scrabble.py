## Scrabble ##

letters = [
  "A", "B", "C", "D", "E", "F", "G",
  "H", "I", "J", "K", "L", "M", "N", 
  "O", "P", "Q", "R", "S", "T", "U", 
  "V", "W", "X", "Y", "Z"
  ]
points = [
  1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 
  4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10
  ]

#2 letters list did not take into account blank tiles. 
#  Add an element to the letter_to_points dictionary 
#  that has a key of " " and a point value of 0
letter_to_points = {
  key:value for key, value in zip(letters, points)
  }
letter_to_points[" "] = 0
#print(letter_to_points)

#3 create a function that will take in a word and 
#  return how many points that word is worth.
#  
#  Define a function called score_word that takes in 
#  a parameter word
def score_word(word):
  point_total = 0 #4

  #5 create a for loop that goes through the letters 
  #  in word and adds the point value of each letter 
  #  to point_total by getting get the point value  
  #  from the letter_to_points dictionary. If a letter 
  #  is not in letter_to_points, add 0 to the 
  #  point_total
  for letter in word:
    a = letter_to_points.get(letter, 0)
    point_total += a
  #print(point_total)
  return point_total #6

#7 Create a variable called brownie_points and set it 
#  equal to the value returned by the score_word() 
#  function with an input of "BROWNIE"
brownie_points = score_word("BROWNIE")
#print("brownie_points", str(brownie_points)) #8

## Score a Game ##

#9 Create a dictionary called player_to_words that maps 
#  players to a list of the words they have played
players_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"], 
  "wordNerd": ["EARTH", "EYES", "MACHINE"], 
  "Lexi Con": ["ERASER", "BELLY", "HUSKY"], 
  "Prof Reader": ["ZAP", "COMA", "PERIOD"]
  }

player_to_points = {} #10 Create an empty dictionary
#print(players_to_words)

#11 Iterate through the items in player_to_words. Call
#   each player player and each list of words words
#
#   Within your loop, create a variable called 
#   player_points and set it to 0.
for player, words in players_to_words.items():
  player_points = 0

  #12 Within the loop, create another loop that goes 
  #   through each word in words and adds the value 
  #   of score_word() with word as an input
  for word in words:
    player_points += score_word(word)
    print("+", player, word)
    
  print("*", player, player_points)

  #13 After the inner loop ends, set the current 
  #   player value to be a key of player_to_points, 
  #   with a value of player_points.
  player_to_points[player] = player_points

#14 player_to_points should now contain the mapping of 
#   players to how many points they’ve scored. Print this 
#   out
print(player_to_points)

print("?", players_to_words.items())

## Further Practice ##
gamers = []
gamer = {}

def add_gamer(gamer, gamers_list):
  if gamer.keys():
    name = gamer.keys()
    availability = gamer.values()
    print("llll", name)
    print("????", availability)
    gamer.update({name: availability})
    
kimberly = {}
kimberly["Kimberly Warner"] = ["x", "n", "c"]
print("::::::", kimberly.keys(), kimberly.values())
#add_gamer(kimberly, "gamers")


