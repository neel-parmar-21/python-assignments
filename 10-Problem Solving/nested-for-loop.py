#1 
n = int(input("Enter a number: "))
mid = n // 2 + 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == 1 or j == n or i == n or (i == mid and j == mid):
            print("*", end="")
        else:
            print(" ", end="")
    print()

#Q1
n = int(input("Enter a number: "))

for i in range(n+1):
    for j in range(n+1):
        print("*", end="")
    print()


#Q2
for i in range(1,4):
    for j in range(1,4):
        print(j, end=" ")
    print()

#Q3
for i in range(1,4):
    for j in range(1,4):
        print(i, end=" ")
    print()

#Q4
n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

#Q5
for i in range(5,0,-1):
    for j in range(i):
        print("*", end= " ")
    print()

#Q6
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#Q7
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

#Q8
n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print()

#Q9
for i in range(1,4):
    for j in range(1,6):
        print(i*j, end=" ")
    print()

#Q10
n = int(input("Enter a number: "))
for i in range(n):
  for j in range(1,6):
    for k in range(2,3):
     print( j ** k, end=" ")
  print()


#Q11
n = int(input("Enter a number: "))
for i in range(1,n + 1):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()

#Q12
n = int(input("Enter a number: "))
for i in range(1,n + 1):
    for j in range(i):
        print(chr(64+i),end=" ")
    print()

#Q13
n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,i*2,2):
        print(j, end= " ")
    print()

#Q14
n = int(input("Enter a number: "))
for i in range(2,n+2):
    for j in range(2,i*2,2):
        print(j, end=" ")
    print() 

#Q15
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

#Q16
for i in range(1,6):
    for j in range(1,6):
        print(j, end=" ")
    print()

#Q17
num = 0
for i in range(3):
    for j in range(3):
        num += 1
        print(num, end=" ")
    print()


#Q18
num = 0
for i in range(4):
  for j in range(5):
      num += 1
      print(num, end=" ")
  print()

#Q19
for i in range(1,4):
    for j in range(1,4):
        print((i,j),end=" ")
    print()

#Q20
for i in range(1,4):
    for j in range(1,4):
        print(i,j, end=" ")
        print()

#Q21
for i in range(1,11):
    for j in range(1,11):
        print(i * j, end=" ")

#Q22
for i in range(1,6):
    for j in range(i):
        print(i, end="")
    print()

#Q23
for i in range(6,1,-1):
    for j in range(1,i):
        print(j, end="")
    print()

#Q24
for i in range(5, 0, -1):
    for j in range(5, 5-i, -1):
        print(j, end="")
    print()

#Q25
for i in range(1,6):
    for j in range(1,6):
        print(i, end="")
    print()