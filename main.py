# File: main.py

courses =  [ [("CS 328", 3.2), ("EDU 221", 4.0), ("HFA 027", 3.5)], [("EDU 225", 3.2), ("CS 321", 4.0), ("HIS 260", 3.4)] ]

gpaSum = 0
classCount = 0
careerGPA = 0
for semester in range(0,2):
    for course in range(0,3):
        classCount = classCount + 1
        gpaSum = gpaSum + courses[semester][course][1]
        careerGPA = gpaSum / classCount
print(careerGPA)