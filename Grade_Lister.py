# A Simple Grade Lister Program #

# Input Sample: "John Ray-85, Carla Davis-100, Ryan Williams-94, Jennifer Martin-89"
inputString = input("\nEnter the Grade Data (Name1-Grade1, Name2-Grade2, ...): ")
rawData = [x.strip() for x in inputString.split(',')]

tempData = {}                  # New Empty Dictionary
for item in rawData:
    tempData[item.split('-')[0]] = item.split('-')[1]          # Assigning Keys-Values to the Dictionary

gradeList = sorted(tempData.items(), key=lambda x: int(x[1]), reverse=True)          # Sorting by Grades

average = 0.0
for element in gradeList:
    average += int(element[1])                 # 1) average = Sum of All the Grades

average = average / len(gradeList)             # 2) average = Sum of All the Grades / Number of Students

print(f"\nAverage Grade:".ljust(21) + f"{average:.2f}")
for name, grade in gradeList:                  # Printing All the Names with Their Grades
    if int(grade) < average:
        print(name.ljust(20) + f"{grade}".ljust(4) + "(Failed)")
    else:
        print(name.ljust(20) + f"{grade}".ljust(4) + "(Passed)")