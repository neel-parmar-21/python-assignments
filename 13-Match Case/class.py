while True:
    print("""
Type of Operations:
1 - Addition
2 - Subtraction
3 - Multiplication
4 - Division
5 - Remainder
6 - Exponentiation
0 - Exit""")

    choice = int(input("Enter the choice to perform the operation: "))

    if choice == 0:
        print("Goodbye!")
        break

    if choice not in range(1, 7):
        print("Invalid choice. Please select 1-6 (or 0 to exit).")
        continue

    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))

    if choice == 1:
        print("Result:", n1 + n2)
    elif choice == 2:
        print("Result:", n1 - n2)
    elif choice == 3:
        print("Result:", n1 * n2)
    elif choice == 4:
        if n2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print("Result:", n1 / n2)
    elif choice == 5:
        if n2 == 0:
            print("Error: Cannot find remainder with zero.")
        else:
            print("Result:", n1 % n2)
    elif choice == 6:
        print("Result:", n1 ** n2)


day = int(input("Enter weekday: "))

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid Day")

marks = int(input("Enter your marks: "))

match marks:
    case x if x >= 90:
        print("A")
    case x if x >= 75:
        print("B")
    case x if x >= 60:
        print("C")
    case x if x >= 40:
        print("D")
    case _:
        print("Fail")


print("""Movie Category Choice:
1. Action
2. Comedy
3. Horror""")

movie = int(float(input("Enter movie category: ")))

if movie == 1:
    print("""1. Fast and Furious
2. Mission Impossible
3. Avengers""")

elif movie == 2:
    print("""1. Welcome
2. Phir Hera Pheri
3. Dhamaal""")

elif movie == 3:
    print("""1. The Conjuring
2. Annabelle
3. Insidious""")

else:
    print("Enter a valid choice!")                                                

if movie in (1, 2, 3):
    choice = int(float(input("Enter movie choice: ")))

    match movie:
        case 1:
            match choice:
                case 1:
                    print("Fast & Furious")
                case 2:
                    print("Mission Impossible")
                case 3:
                    print("Avengers")
                case _:
                    print("Invalid movie option!")

        case 2:
            match choice:
                case 1:
                    print("Welcome")
                case 2:
                    print("Phir Hera Pheri")
                case 3:
                    print("Dhamaal")
                case _:
                    print("Invalid movie option!")

        case 3:
            match choice:
                case 1:
                    print("The Conjuring")
                case 2:
                    print("Annabelle")
                case 3:
                    print("Insidious")
                case _:
                    print("Invalid movie option!")

