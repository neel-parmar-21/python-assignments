string = input("Enter a string: ")

i = 0
j = len(string) - 1

flag = True

while(i < j) and flag:

    if string[i] == string[j]:
        i += 1
        j -= 1
    else:
        flag = False

if flag:
    print("String is Pallindrome")
else:
    print("String is not Pallindrome") 

number = int(input("Enter a number: "))

while number > 0:
    digit = number % 10
    print(digit, end="")
    number = number // 10

row = 1

while row <= 3:
    column = 1

    while column <= 4:
        print("*", end="")
        column += 1

    row += 1
    print()

string = input("Enter a string: ").strip()
digits = "0123456789"
result = ""

for i in string:
    if i not in digits:
        result = result + i

print(result)   

string = input("Enter a string: ")

count = 0

for i in string:
    if i.islower():
        count += 1

print(count)

str = "abc123"

print(str.isdigit())







    
