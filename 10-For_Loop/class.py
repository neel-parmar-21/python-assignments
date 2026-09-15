number = int(input("Enter a number: "))

for i in range(1,11):
    print(f"{number} x {i} = {number * i}")

string = input("Enter a string: ").strip().lower()

length = len(string) - 1

sum = ""

for i in range(length, -1, -1):
    sum = sum + string[i]

if string == sum:
    print("String is Palindrome")
else:
    print("String is not Palindrome")

n = input("Enter a number: ")
sum = 0
for i in range(0,len(n)):
    sum = sum + int(n[i]) ** 3

if int(n) == sum:
    print("Armstrong Number")
else:
    print("Not an armstrong number")










