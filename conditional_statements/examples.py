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
'''
'''

Write a Python program that classifies a person's age into one of the following categories: 
"Infant," "Child," "Teenager," "Adult," or "Senior." 
The program should ask the user for their age and then display the corresponding classification based on the following guidelines:

    Infants: 0-2 years old
    Children: 3-12 years old
    Teenagers: 13-19 years old
    Adults: 20-64 years old
    Seniors: 65 years old and older
'''

'''age = int(input("Please enter your age: "))

if age >= 0 and age <= 2:
    print("Infant")
elif age >= 3 and age <= 12:
    print("Children")
elif age >= 13 and age <= 19:
    print("Teenagers")
elif age >= 20 and age <= 64:
    print("Adults")
else:
    print("Seniors")'''

'''
A leap year is a calendar year containing an additional day added to keep the calendar year synchronized with the astronomical or 
seasonal year. 
In the Gregorian calendar, each leap year has 366 days instead of 365, by extending February to 29 days rather than the common 28. 
These extra days occur in years which are multiples of four (with the exception of centennial years not divisible by 400). 
Write a Python program, which asks for a year and calculates, if this year is a leap year or not.
'''
'''year = int(input("Enter the year to see if it is leap year or not: "))

if (year % 4 == 0 and year % 100 != 0)or (year % 400 != 0):
    print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year!")'''

