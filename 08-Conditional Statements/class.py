username = input("Enter your username: ")
password = input("Enter your password: ")
age = int(input("Enter your age: "))
terms= input("Do you accept the terms and conditions: ")

if username=="Neel":
    if password=="python123":
        if age>=18:
            if terms!="yes":
                print("Accept the terms and conditions first!!")
                if terms=="yes":
                    print("Login Successful! Welcome!")

print("18"==18)
print("18">=18)

is_indian = input("Are you Indian? YES or No: ")

if is_indian == "Yes":
    print("Welcome to our team!")
    
else:
    if is_indian == "No":
        print("You're not selected")
    else:
        print("Enter a valid value")

marks = int(input("Enter your marks: "))

if marks > 89:
    print("A")

elif marks > 74:
    print("B")

elif marks > 59:
    print("C")

elif marks > 39:
    print("D")

else:
    print("F")

print("1 = Addition""\n"
      "2 = Subtraction""\n"
      "3 = Multiplication""\n"
      "4 = Division"
       )

operation = int(input("Enter the mode of operation you want to perform: "))
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if operation == 1:
    print(f"Addition: {number1 + number2}")

elif operation == 2:
    print(f"Subtraction: {number1 - number2}")

elif operation == 3:
    print(f"Multiplication: {number1 * number2}")

elif operation == 4:
    print(f"Division: {number1 / number2}")

else:
    print("Enter a valid operation number")











