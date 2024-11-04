courses = ["MIT", "Cybersec","Datasci"]
print(courses)

#Accessing array elements
print(courses[0])

#Looping through an array
for y in courses:
    print("course is:",y)

#Adding a new element to an array
courses.append("Computer Science")
print(courses)

#Removing an element
courses.remove("MIT")
print(courses)