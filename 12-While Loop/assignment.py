# 1
i = 1
while i <= 5:
    print("Hello")
    i += 1

# 2
i = 0
while i < 10:
    print(i, end=" ")
    i += 1
print()

# 3
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()

# 4
i = 10
while i >= 1:
    print(i, end=" ")
    i -= 1
print()

# 5
i = 5
while i <= 50:
    print(i, end=" ")
    i += 5
print()

# 6
i = 2
while i <= 20:
    print(i, end=" ")
    i += 2
print()

# 7
i = 1
while i <= 19:
    print(i, end=" ")
    i += 2
print()

# 8
i = 3
while i <= 18:
    print(i, end=" ")
    i += 3
print()

# 9
i = 20
while i >= 2:
    print(i, end=" ")
    i -= 2
print()

# 10
n = int(input("Enter a positive number: "))
i = 1
while i <= n:
    print(i, end=" ")
    i += 1
print()

# 11
n = int(input("Enter n: "))
i = 1
while i <= n:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
print()

# 12
n = int(input("Enter n: "))
i = 1
while i <= n:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1
print()

# 13
n = int(input("Enter n: "))
i = 1
while i <= n:
    if i % 3 == 0:
        print(i, end=" ")
    i += 1
print()

# 14
n = int(input("Enter n: "))
i = 1
while i <= n:
    if i % 2 == 0 and i % 3 == 0:
        print(i, end=" ")
    i += 1
print()

# 15
n = int(input("Enter n: "))
i = 1
count = 0
while i <= n:
    if i % 2 == 0:
        count += 1
    i += 1
print("Count of even numbers:", count)

# 16
n = int(input("Enter n: "))
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print("Sum:", total)

# 17
n = int(input("Enter n: "))
i = 1
total = 0
while i <= n:
    if i % 2 == 0:
        total += i
    i += 1
print("Sum of even numbers:", total)

# 18
n = int(input("Enter n: "))
i = 1
total = 0
while i <= n:
    if i % 2 != 0:
        total += i
    i += 1
print("Sum of odd numbers:", total)

# 19
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1

# 20
n = int(input("Enter n: "))
i = 1
fact = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial:", fact)

# 21
text = input("Enter a string: ")
i = 0
while i < len(text):
    print(text[i])
    i += 1

# 22
text = input("Enter a string: ")
i = 0
while i < len(text):
    print(text[i], end="")
    i += 1
print()

# 23
text = input("Enter a string: ")
i = 0
count = 0
while i < len(text):
    count += 1
    i += 1
print("Number of characters:", count)

# 24
text = input("Enter a string: ")
i = 0
count = 0
while i < len(text):
    if text[i] == "a":
        count += 1
    i += 1
print("Occurrences of a:", count)

# 25
text = input("Enter a string: ")
i = 0
count = 0
while i < len(text):
    if text[i] >= "A" and text[i] <= "Z":
        count += 1
    i += 1
print("Uppercase letters:", count)

# 26
row = 1
while row <= 3:
    col = 1
    while col <= 4:
        print("*", end="")
        col += 1
    print()
    row += 1

# 27
row = 1
while row <= 4:
    col = 1
    while col <= 5:
        print("*", end="")
        col += 1
    print()
    row += 1

# 28
row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    print()
    row += 1

# 29
row = 1
while row <= 5:
    col = 1
    while col <= row:
        print(col, end="")
        col += 1
    print()
    row += 1

# 30
row = 1
while row <= 5:
    col = 1
    while col <= 5:
        print(row * col, end=" ")
        col += 1
    print()
    row += 1

# Final Challenge
n = int(input("Enter n: "))
row = 1
while row <= n:
    col = 1
    while col <= row:
        print(col, end="")
        col += 1
    print()
    row += 1
