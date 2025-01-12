# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Write your code below: 

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * (5/9)
  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp = (c_temp * 9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

def get_force(mass, acceleration):
  return mass * acceleration
  
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass, c=3*10**8):
  return mass * c

bomb_energy = get_energy(bomb_mass) 
print("“A 1kg bomb supplies", str(bomb_energy), "Joules.")

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration) * distance
  return force

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does" + str(train_work), "Joules of work over", train_distance, "meters.")

## Review ##
#1 Define a class named Student that will be our data model at Jan van Eyck High School and Conservatory
class Student():
  #1 Add a constructor for Student. Have the constructor take in two parameters: a name and a year
  def __init__(self, name, year):
    self.name = name
    self.year = year
    #5 In constructor for Student, declare self.grades as an empty list
    self.grades = []
#6 Add an .add_grade() method to Student that takes a parameter, grade
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)

#2 Create three instances of the Student class, Save them into the variables roger, sandro, and pieter
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

#3 Create a Grade class, with .minimum_passing as an attribute set to 65.
class Grade():
  minimum_passing = 65
  #4 Give Grade a constructor with one parameter score and assign score to self.score
  def __init__(self, score):
    self.score = score

#7 Create a new Grade with a score of 100 and add it to pieter‘s .grades attribute using .add_grade()
pieter.add_grade(Grade(100))












