'''
Write a Python program that checks the temperature and provides a message based on the 
temperature value. 

If the temperature is above 27 degrees Celsius, it should print "It's a hot day." 
If the temperature is 27 degrees or below, it should print "It's not a hot day."
'''
'''
temperature = int(input("Enter the temperature: "))

if temperature > 27:
    print("it's a hot day!")
else:
    print("it's not a hot day")
'''
'''
Write a Python program that calculates and displays a letter grade for a given numerical score based on the following grading scale:

    A: 90-100
    B: 80-89
    C: 70-79
    D: 60-69
    F: 0-59
'''

score = int(input("Enter the score: "))

if score >= 90 and score <= 100:
    print("Your grade is A")
elif score >= 80 and score < 90:
    print("Your grade is B")
elif score >= 70 and score < 80:
    print("Your grade is C")
elif score >= 60 and score < 70:
    print("Your grade is D")
else:
    print("Your grade is F")



