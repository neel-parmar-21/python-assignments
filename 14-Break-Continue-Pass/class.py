str = input("Enter a string: ").strip().lower()
flag = False
count = 0
for i in str:
    if i == "o" and count < 1:
        flag = True
        print("Found")
        break

if not flag:
    print("Not found")


# 1
for i in range(1,11):
    if i == 6:
        break
    print(i)

# 2
numbers = [10, 20, 30, 40, 50]

for i in numbers:
    if i == 30:
        break
    print(i)


# 3
i = 0
while i <= 0:
    number = int(input("Enter a number: ").strip())
    if number == 0:
        break

# 4
for i in range(1,101):
    if i % 17 == 0:
        break
    print(i)

 

