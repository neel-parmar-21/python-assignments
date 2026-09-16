#LEVEL 1 - INTERMEDIATE

#1. Positive, Negative, or Zero
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
elif number == 0:
    print("Zero")

#2. Even or Odd + Positive or Negative
number = int(input("Enter a number: "))

if number > 0 :
    if number % 2 == 0:
        print("Positive Even")
    else:
        print("Negative Odd")

elif number < 0:
    if number % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")
else:
    print("Zero")

#3. Largest of Two Numbers
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

if number_1 > number_2:
    print("Number 1 is greater")
elif number_2 > number_1:
    print("Number 2 is greater")

elif number_1 == number_2:
    print("Both are equal")

#4. Smallest of Three Numbers
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))

if number_1 == number_2 == number_3:
    print("All numbers are equal")
elif number_1 <= number_2 and number_1 <= number_3:
    print("First number is the smallest")
elif number_2 <= number_1 and number_2 <= number_3:
    print("Second number is the smallest")
elif number_3 <= number_1 and number_3 <= number_2:
    print("Third number is the smallest")

#5. Largest of Three Numbers
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))

if number_1 == number_2 == number_3:
    print("All numbers are equal")
elif number_1 >= number_2 and number_1 >= number_3:
    print("First number is the largest")
elif number_2 >= number_1 and number_2 >= number_3:
    print("Second number is the largest")
elif number_3 >= number_1 and number_3 >= number_2:
    print("Third number is the largest")

#6. Divisible by 5 and 11
number = int(input("Enter a number: "))

if number % 5 == 0 and number % 11 == 0:
    print("Divisible by both 5 and 11")
elif number % 5 == 0:
    print("Divisible by only 5")
elif number % 11 == 0:
    print("Divisible by only 11")
else:
    print("Divisible by neither")

#7. Divisible by Either 3 or 7
number = int(input("Enter a number: "))

if number % 3 == 0 and number % 7 == 0:
    print("Divisible by either 3 or 7")
elif number % 3 == 0:
    print("Divisible by only 3")
elif number % 7 == 0:
    print("Divisible by only 7")
else:
    print("Divisible by neither")

#8. Pass or Fail
marks = int(input("Enter your marks: "))

if marks < 0:
    print("Invalid marks")
elif marks > 100:
    print("Invalid marks")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")

#9. Grade Calculator
marks = int(input("Enter your marks: "))
if marks < 0:
    print("Invalid marks")
elif marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
elif marks >= 40:
    print("E")
else:
    print("Fail")

#10. Voting Eligibility
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
if age > 120:
    print("Invalid age")
elif age < 18:
    print("Cannot vote")
elif age >= 18:
    print("Can vote")
else:
    print("Enter a valid age")


#LEVEL 2 — MORE LOGICAL CONDITIONS
#11. Leap Year
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap Year")
else:
    print("Not a leap year")
    

#12. Character Type
char = input("Enter a character: ").lower()

if char >= 65 and char <= 90:
    print("Uppercase alphabet")
elif char >= 97 and char <= 122:
    print("Lowercase alphabet")
elif char >= 48 and char <= 57:
    print("Digit")
else:
    print("Special Character")

# 13. Vowel or Consonant

char = input("Enter a character: ").lower()

ascii_value = ord(char)

if ascii_value >= 97 and ascii_value <= 122:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")

#14. Profit or Loss
cost_price = int(input("Enter the cost price: "))
selling_price = int(input("Enter the selling price: "))

profit = selling_price - cost_price
loss = cost_price - selling_price

if selling_price > cost_price:
    print(f"Profit: {profit}")
elif cost_price > selling_price:
    print(f"Loss: {loss}")
else:
    print("No profit and no loss")

#15. Profit/Loss Percentage
cost_price = int(input("Enter the cost price: "))
selling_price = int(input("Enter the selling price: "))

if cost_price <= 0:
    print("Invalid cost price")
else:
    profit = selling_price - cost_price
    loss = cost_price - selling_price

    if selling_price > cost_price:
     profit_percentage = profit / cost_price * 100
     print(f"Profit Percentage: {profit_percentage}")
    elif cost_price > selling_price:
     loss_percentage = loss / cost_price * 100
     print(f"Loss Percentage: {loss_percentage}")
    else:
     print("No profit and no loss")

#16
units = int(input("Enter your electricity bill units: "))
bill = 1

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10

print(f"Your electricity bill is {bill} rupees.")

#17
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operator= input("Choose the operator: ")
result = 1

if operator == "+":
    result = first_number + second_number
    print(result)
elif operator == "-":
    result = first_number - second_number
    print(result)
elif operator == "*":
    result = first_number * second_number
    print(result)
elif operator == "/":
    if second_number != 0:
        result = first_number / second_number
        print(result)
    else:
        print("Division by Zero isn't allowed.")

#18
temperature = int(input("Enter the temperature in Celsius: "))

if temperature < 0:
    print("Freezing")
elif temperature >= 0 and temperature <= 15:
    print("Very Cold")
elif temperature >= 16 and temperature <= 25:
    print("Cold")
elif temperature >= 26 and temperature <= 35:
    print("Normal")
else:
    print("Hot")

#19
number = int(input("Enter a number: "))

if number < 0:
    print("Negative")
elif number >= 0 and number <= 10:
    print("Number is between 0 and 10")
elif number >= 11 and number <= 50:
    print("Number is between 11 and 50")
elif number >= 51 and number <= 100:
    print("Number is between 51 and 100")
else:
    print("Above 100")

#20
a = int(input("Enter first side length: "))
b = int(input("Enter second side length: "))
c = int(input("Enter third side length: "))

if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Invalid triangle")


#LEVEL 3 - HARDER CONDITIONAL PROBLEMS

#21
a = int(input("Enter first side length: "))
b = int(input("Enter second side length: "))
c = int(input("Enter third side length: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or c == a:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")

else:
    print("Invalid triangle")

# #22
balance = int(input("Enter the account balance: "))
amount = int(input("Enter the withdrawal amount: "))
remaining_amount = balance - amount 

if amount > 0:
    if amount <= balance:
        if amount % 100 == 0:
             if remaining_amount >= 500:
                 print("Withdrawal Successful")
                 print(f"Remaining balance: ₹{remaining_amount}")
             else:
                 print(f"Your available balance: {remaining_amount} After withdrawal, a minimum balance of ₹500 must remain in your account.")
        else:
            print("Please enter an amount divisible by 100.")
    else:
       print(f"Insufficient funds. Your available balance is ₹ {balance}.")
else:
    print("Withdrawal amount must be greater than 0.")

#23
username = input("Enter your username: ")
password = input("Enter your password: ")

if username != "admin":
    print("User not found")
elif password != "python123":
    print("Wrong password")
else:
    print("Login successful")

#24
purchase_amount = float(input("Enter the purchase amount: "))
discount_percentage = "0%"
if purchase_amount < 500:
    discount = 0
elif purchase_amount >= 500 and purchase_amount <= 999:
    discount_percentage = "5%"
    discount = purchase_amount * 0.05
elif purchase_amount >= 1000 and purchase_amount <= 1999:
    discount_percentage = "10%"
    discount = purchase_amount * 0.1
elif purchase_amount >= 2000 and purchase_amount <= 4999:
    discount_percentage = "15%"
    discount = purchase_amount * 0.15
else:
    discount_percentage = "20%"
    discount = purchase_amount * 0.2

final_amount = purchase_amount - discount

print(f"Purchase: {purchase_amount}")
print(f"Discount: {discount_percentage}")
print(f"Discount Amount: ₹{discount}")
print(f"Final amount: ₹{final_amount}")

#25
marks_1 = int(input("Enter first subject marks: "))
marks_2 = int(input("Enter second subject marks: "))
marks_3 = int(input("Enter third subject marks: "))

average = 0

if marks_1 >= 0 and marks_1 <= 100  and marks_2 >= 0 and marks_2 <= 100 and marks_3 >= 0 and marks_3 <= 100:

    if marks_1 >= 35 and marks_2 >= 35 and marks_3 >= 35:

        average = (marks_1 + marks_2 + marks_3) / 3 

        if average >= 75:
            print("Distinction")

        elif average >= 60:
            print("First Class")

        elif average >= 50:
            print("Second Class")

        else:
            print("Pass")

    else:
        print("Fail")

else:
    print("Invalid marks")

#26 
date = int(input("Enter date: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

leap_year = 0

if year % 400 == 0:
    leap_year = 1
elif year % 4 == 0 and year % 100 != 0:
    leap_year = 1

if year >= 1 and year <= 9999:
    if month >= 1 and month <= 12:

        if month == 2:
            if leap_year == 1:
                if date >= 1 and date <= 29:
                    print("Valid")
                else:
                    print("Invalid")
            else:
                if date >= 1 and date <= 28:
                    print("Valid")
                else:
                    print("Invalid")

        elif month == 4 or month == 6 or month == 9 or month == 11:
            if date >= 1 and date <= 30:
                print("Valid")
            else:
                print("Invalid")

        else:
            if date >= 1 and date <= 31:
                print("Valid")
            else:
                print("Invalid")

    else:
        print("Invalid")
else:
    print("Invalid")

#27
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

if hours >= 0 and hours <= 23:
    if minutes >= 0 and minutes <= 59: 
         if seconds >= 0 and seconds <= 59:
              print("Valid time")
else:
     print("Invalid time")

#28
name_1 = input("Enter first person's name: ")
age_1 = int(input("Enter first person's age: "))

name_2 = input("Enter second person's name: ")
age_2 = int(input("Enter second person's age: "))

name_3 = input("Enter third person's name: ")
age_3 = int(input("Enter third person's age: "))


if age_1 == age_2 == age_3:
    print("All three have the same age.")

elif age_1 == age_2 or age_2 == age_3 or age_3 == age_1:
    print("Two people have the same age.")

elif age_1 < age_2 and age_1 < age_3:
    print(f"{name_1} is the youngest")

elif age_2 < age_1 and age_2 < age_3:
    print(f"{name_2} is the youngest")

elif age_3 < age_1 and age_3 < age_2:
    print(f"{name_3} is the youngest")

#29
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    if b > c:
        second = b
    else:
        second = c

elif b > a and b > c:
    if a > c:
        second = a
    else:
        second = c

else:
    if a > b:
        second = a
    else:
        second = b

print("Second largest number:", second)

#30
age = int(input("Age: "))
marks = int(input("Marks: "))
income = int(input("Income: "))
attendance = int(input("Attendance: "))

if age >= 18 and age <= 25:

    if marks >= 85:

        if attendance >= 75:

            if income <= 300000:
                print("Scholarship Approved")

            else:
                print("""Scholarship Rejected
Reason: Family income above ₹300000""")

        else:
            print("""Scholarship Rejected
Reason: Attendance below 75%""")

    else:
        print("""Scholarship Rejected
Reason: Marks below 85""")
        
else:
    print("""Scholarship Rejected
Reason: Age must be between 18 and 25""")

                


     




