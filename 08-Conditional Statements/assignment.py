#Task 1
number = int(input("Enter a number: "))
if number > 10:
    print("Greater than 10")

#Task 2
age = int(input("Enter your age: "))
if age >= 18:
    print("Adult")

#Task 3
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")

#Task 4
marks = int(input("Enter your marks: "))
if marks >= 40:
    print("Pass")

#Task 5
number = int(input("Enter a number: "))
if number == 0:
    print("Zero")

#Task 6
number = int(input("Enter a number: "))
if number >= 0:
    print("Positive")
else:
    print("Not positive")

#Task 7
age = int(input("Enter your age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")

#Task 8
number = int(input("Enter a number to check whether it's even or odd: "))
if number % 2 == 0:
    print("This number is even.")
else:
    print("This number is odd.")

#Task 9
marks = int(input("Enter your marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")

#Task 10
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if number_1 > number_2:
    print("First number is greater")
else:
    print("Second number is greater")

#Task 11
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F")

#Task 12
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

#Task 13
print("""1 → Monday
2 → Tuesday
3 → Wednesday
4 → Thursday
5 → Friday""")

number = int(input("Enter the number representing the day: "))

if number == 1:
    print("Monday")
elif number == 2:
    print("Tuesday")
elif number == 3:
    print("Wednesday")
elif number == 4:
    print("Thursday")
elif number == 5:
    print("Friday")
else:
    print("Other")

#Task 14
marks = int(input("Enter your marks: "))

if marks >= 80:
    print("Excellent")
elif marks >= 60:
    print("Good")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")

#Task 15
number = int(input("Enter a number: "))

if number == 1:
    print("1")
elif number == 2:
    print("2")
elif number == 3:
    print("3")
else:
    print("Other")

#Task 16
age = int(input("Enter your age: "))

if age >= 18:
    if age <= 60:
        print("Between 18 and 60")

#Task 17
marks = int(input("Enter your marks: "))
if marks >= 40:
    if marks >= 75:
        print("Good")
    else:
        print("Passed")

else:
    print("Failed")

#Task 18
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
    if number > 100:
        print("Greater than 100")

#Task 19
age = int(input("Enter your age: "))

if age >= 18:
    print("You're an adult")
    if age >= 60:
        print("You're a senior citizen")

#Task 20
number = int(input("Enter a number: "))

if not number == 0:
    if number > 0:
        print("Positive")
    else:
        print("Negative")

#Task 21
age = int(input("Enter your age: "))
marks = int(input("Enter your marks"))

if age >= 18:
    if marks >= 40:
        print("Eligible")

#Task 22
number = int(input("Enter a number: "))

if number < 10:
    print("Special")

elif number > 100:
    print("Special")

#Task 23
age = int(input("Enter your age: ")) >= 18
has_id = input("Do you have id? True or False: ").lower() == "true"

if age and has_id:
    print("Allowed")
else:
    print("Not Allowed")

#Task 24
number_1 = int(input("Enter the first number: ")) > 10
number_2 = int(input("Enter the second number: ")) > 10

if number_1 and number_2:
    print("Both are greater than 10")
else:
    print("Both are less than 10")

#Task 25
number = int(input("Enter the number to check whether it's less than 0 or greater than 100: ")) 

if number < 0:
    print("Less than 0")
elif number > 100:
    print("Greater than 100")
else:
    print("Please enter a valid value!")

#Task 26
is_closed = False

if  not is_closed:
    print("Open")
else:
    print("Closed")

#Task 27
number = int(input("Enter a number: "))

if number >= 10 and number <= 50:
    print("It is between 10 and 50")
else:
    print("It is not between 10 and 50")

#Task 28
number = int(input("Enter a number: "))

if number < 10 or number > 50:
    print("It is outside the range")
else:
    print("It is inside the range")

#Task 29
is_student = input("Are you a student? Yes or No: ").lower() == "yes" 
has_id = input("Do you have student id? Yes or No: ").lower() == "yes"
has_ticket = input("Are you have ticket? Yes or No: ").lower() == "yes"

if is_student and has_id and has_ticket:
    print("Allowed")
else:
    print("Not Allowed")

#Task 30
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
has_id = input("Do you have id? Yes or No: ") == "True"

if age >= 18 and marks >= 40 and has_id:
    print("Eligible")
else:
    print("Not eligible")

# and is appropriate because we have to satify all the conditions.








