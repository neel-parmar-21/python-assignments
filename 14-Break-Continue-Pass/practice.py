# 31. Practice Problems: break

# #1
# for i in range(1,11):
#     if i == 6:
#         break
#     print(i)

# #2
# numbers = [10, 20, 30, 40, 50]

# for i in numbers:
#     if i == 30:
#         print("Found")
#         break

# #3 
# i = 0

# while i <= 0:
#     number = int(input("Enter a number: "))
#     if number == 0:
#         break

# #4 
# for i in range(1,101):
#     if i % 17 == 0:
#         break
#     print(i)

# 32. Practice Problems: continue

# #1
# for i in range(1,31):
#     if i % 2 == 0:
#         continue
#     print(i)

# #2 
# numbers = [10, -2, 30, -5, 40, -8]

# for i in numbers:
#     if i < 0:
#         continue
#     print(i)

# #3
# for i in range(1,21):
#     if i % 3 == 0:
#         continue
#     print(i)

# #4 
# numbers = [5, 12, 8, 21, 30, 7]

# for i in numbers:
#     if i < 10:
#         continue
#     print(i)

# #5
# number = int(input("Enter a number: "))
# if number > 0:
#     pass

# 34. Mixed Practice Problems

#1
# Output - 1
#          2

#2 
# Output - 1
#          2
#          4
#          5

#3
# Output - 1
#          2
#          3
#          4
#          5

#4
# Output - prints 1 and 2 then infinite loop because we didn't updated the i 

#5
# Output - 1
#          2

#6
# Output - prints nothing

#7
# Output - Done

# 35. Challenge Problems


# #1

# i = 0
# while i <= 0:
#     number = int(input("Enter a number: "))
#     if number > 0:
#         print(number)
#     elif number < 0:
#         continue
#     else:
#         break

# #2

# numbers = [12, 5, -4, 18, 0, 25, 30]

# for i in numbers:
#     if i > 0:
#         print(i)
#     elif i < 0:
#         continue
#     else:
#         break 

#3

arr = ["Aryan", 18, True]

for i in arr:
    if type(i) == int:
        print("Number found")
        break
else:
    print("Number not found")
    












