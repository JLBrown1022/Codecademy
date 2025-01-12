last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook, "\n")
new_grade = ["computer science", 100]
gradebook.append(new_grade)
print(gradebook, "\n")
new_grade = ["visual arts", 93]
gradebook.append(new_grade)
print(gradebook, "\n")
gradebook[-1][-1] += 5
print(gradebook, "\n")

#gradebook[2].remove("poetry")
gradebook[2].remove(85)
print(gradebook, "\n")

gradebook[2].append("Pass")
print(gradebook, "\n")

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook, "\n")







