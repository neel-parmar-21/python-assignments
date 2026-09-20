# A. Basic for Loop

#1 
for i in range(1,6):
    print("Hello")

#2 
for i in range (0,10):
    print(i, end=" ")

#3
for i in range (1,11):
    print(i)

#4
for i in range(10,0,-1):
    print(i)

#5
for i in range (5,51,5):
    print(i)

#B. range() Practice

#6
for i in range(2,21,2):
    print(i)

#7
for i in range (1,20,2):
    print(i)

#8
for i in range (3,19,3):
    print(i, end=" ")

#9 
for i in range (20,0,-2):
    print(i)

#10
n = int(input("Enter a positive integer: "))

for i in range(1,n + 1):
    print(i)

#11
n = int(input("Enter a number: "))
for i in range(1,n + 1):
    if i % 2 == 0:
        print(i)

#12
n = int(input("Enter a number: "))
for i in range(1,n + 1):
    if i % 2 == 1:
        print(i)

#13
n = int(input("Enter a number: "))
for i in range(1,n + 1):
    if i % 3 == 0:
        print(i)

#14
n = int(input("Enter a number: "))
for i in range(1,n + 1):
    if i % 2 == 0 and i % 3 == 0:
        print(i)

#15
n = int(input("Enter a number: "))

count = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        count = count + 1
print(count)

#16

n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print(total)

#17 

n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        total = total + i

print(total)

#18 
n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    if i % 2 != 0: # or if i % 2 == 1
        total = total + i

print(total)

#19
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

#20
n = int(input("Enter a nunber: "))

product = 1

for i in range(1, n + 1):
    product = product = product * i

# print(product)

#21
string = input("Enter a string: ")

for i in string:
    print(i)

#22 
string = input("Enter a string: ")

for i in string:
    print(i, end="")


#23
string = input("Enter a string: ")
count = 0

for i in string:
    count = count + 1

print(count)

#24
string = input("Enter a string: ")
count = 0

for i in string:
    if i == "a":
        count = count + 1

print(count)

#25 
string = input("Enter a string: ")
count = 0

for i in string:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        count = count + 1

print(count)

#26
for i in range(3):
    for j in range(4):
        print("*",end="")
    print("")

#27
for i in range(4):
    for j in range(5):
        print("*",end="")
    print("")

#28
for i in range(1,6):
    print("*" * i)

#29
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print("")

#30
for i in range(1,6):
    for j in range(1,11):
        print(j*i, end=" ")
    print("")

#FINAL CHALLENGE
n= int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print("")






    








