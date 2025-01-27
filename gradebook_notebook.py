last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

# Create a list called subjects
subjects = ["physics", "calculus", "poetry", "history"]

# Create a list called grades
grades = [98, 97, 85, 88]

# Create a two dimensional list combining subjects and grades
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# Print gradebook
print(gradebook)

# Add a new score for computer science
gradebook.append(["computer science", 100])
print(gradebook)

# Add new score for visual arts
gradebook.append(["visual arts", 93])
print(gradebook)

# Modify visual arts grade
gradebook[-1][-1] = 98
print(gradebook)

# Remove poetry grade
gradebook[2].remove(85)
print(gradebook)

# Add pass to poetry grade
gradebook[2].append("Pass")
print(gradebook)

# Combine last semester grades with this semester grades
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)