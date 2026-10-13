# Q1
choice = int(input("Enter your choice: "))
match choice:
    case 1:
        print("pizza")
    case 2:
        print("Burger")
    case 3:
        print("pasta")
    case 4:
        print("sandwich")
    case _:
        print("Invalid menu choice")

# Q2
choice = int(input("Enter choice: "))
match choice:
    case 1:
        print("Wifi")
    case 2:
        print("Bluetooth")
    case 3:
        print("Mobile Data")
    case 4:
        print("airplane Mode")
    case 5:
        print("Exit")
    case _:
        print("Invalid setting")

# Q3
choice = int(input("Enter choice: "))
match choice:
    case 1:
        print("Check balance")
    case 2:
        print("Withdraw money ")
    case 3:
        print("Deposit money ")
    case 4:
        print("Change PIN ")
    case 5:
        print("Exit ")
    case _:
        print("Invalid choice")

# Q4
signal = input("Enter signal: ")
match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid aignal")

# Q5
choice = int(input("Enter choice: "))
match choice:
    case 1:
        print("Profile")
    case 2:
        print("Courses")
    case 3:
        print("Marks")
    case 4:
        print("Attendance")
    case 5:
        print("Logout")
    case _:
        print("Invalid choice")

# Q6
choice = int(input("Enter category: "))
match choice:
    case 1:
        print("Electronics")
    case 2:
        print("Clothing")
    case 3:
        print("Books")
    case 4:
        print("Grocery")
    case 5:
        print("Exit ")
    case _:
        print("Invalid Category")

# Q7
choice = int(input("Enter service: "))
match choice:
    case 1:
        print("Account balance")
    case 2:
        print("Mini statement")
    case 3:
        print("Fund transfer")
    case 4:
        print("Bill payment")
    case 5:
        print("Customer support")
    case _:
        print("Invalid service")

# Q8
choice = int(input("Enter show: "))
match choice:
    case 1:
        print("Morning show ")
    case 2:
        print("Afternoon show ")
    case 3:
        print("Evening show ")
    case 4:
        print("Night show ")
    case _:
        print("Invalid show")

# Q9
weather = input("Enter weather: ")
match weather:
    case "sunny":
        print("Wear sunglasses")
    case "rainy":
        print("Carry an umbrella")
    case "cloudy":
        print("Weather may change")
    case "snowy":
        print("Wear warm clothes")
    case _:
        print("Unknown weather")

# Q10
payment = input("Enter payment method: ")
match payment:
    case "upi":
        print("UPI")
    case "card":
        print("Card")
    case "cash":
        print("Cash")
    case "wallet":
        print("Wallet")
    case _:
        print("Invalid payment method")

# Q11
extension = input("Enter extension: ")
match extension:
    case "pdf":
        print("Document file")
    case "jpg" | "png":
        print("Image file")
    case "mp3":
        print("Audio file")
    case "mp4":
        print("Video file")
    case _:
        print("Unknown file")

# Q12
role = input("Enter role: ")
match role:
    case "admin":
        print("Full access")
    case "teacher":
        print("Teacher")
    case "student":
        print("Student")
    case "guest":
        print("Limited access")
    case _:
        print("Invalid role")

# Q13
day = int(input("Enter day number: "))
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid day")

# Q14
priority = int(input("Enter priority: "))
match priority:
    case 1 | 2:
        print("Normal")
    case 3 | 4:
        print("Urgent")
    case _:
        print("Invalid")

# Q15
membership = int(input("Enter membership level: "))
match membership:
    case 1 | 2:
        print("Basic membership")
    case 3 | 4:
        print("Premium membership")
    case _:
        print("Invalid membership")

# Q16
user_type = int(input("Enter user type (1 Student, 2 Teacher): "))
match user_type:
    case 1:
        option = int(input("1 View courses, 2 View marks, 3 View attendance: "))
        match option:
            case 1:
                print("Student courses")
            case 2:
                print("Student marks")
            case 3:
                print("Student attendance")
            case _:
                print("Invalid student option")
    case 2:
        option = int(input("1 View Students, 2 Enter Marks, 3 View Attendance: "))
        match option:
            case 1:
                print("Students")
            case 2:
                print("Enter marks")
            case 3:
                print("Teacher attendance")
            case _:
                print("Invalid teacher option")
    case _:
        print("Invalid user")

# Q17
account = int(input("Enter account type (1 Savings, 2 Current): "))
match account:
    case 1:
        print("Savings account")
        operation = int(input("1 Check balance, 2 deposit, 3 withdraw: "))
        match operation:
            case 1:
                print("Check Balance ")
            case 2:
                print("Deposit ")
            case 3:
                print("Withdraw ")
            case _:
                print("Invalid operation")
    case 2:
        print("Current Account")
        operation = int(input("1 Check Balance, 2 Deposit, 3 Withdraw: "))
        match operation:
            case 1:
                print("Check Balance ")
            case 2:
                print("Deposit ")
            case 3:
                print("Withdraw ")
            case _:
                print("Invalid operation")
    case _:
        print("Invalid account")

# Q18
category = int(input("Enter category (1 Electronics, 2 Clothing): "))
match category:
    case 1:
        product = int(input("1 Mobile, 2 Laptop, 3 Headphones: "))
        match product:
            case 1:
                print("Mobile ")
            case 2:
                print("Laptop ")
            case 3:
                print("Headphones ")
            case _:
                print("Invalid product")
    case 2:
        product = int(input("1 Shirt, 2 Jeans, 3 Shoes: "))
        match product:
            case 1:
                print("Shirt")
            case 2:
                print("Jeans")
            case 3:
                print("Shoes")
            case _:
                print("Invalid product")
    case _:
        print("Invalid category")

# Q19
category = int(input("Enter category (1 Vegetarian, 2 Non-Vegetarian): "))
match category:
    case 1:
        food = int(input("1 Paneer, 2 Dal, 3 Veg Biryani: "))
        match food:
            case 1:
                print("Paneer")
            case 2:
                print("Dal")
            case 3:
                print("Veg biryani")
            case _:
                print("Invalid food choice")
    case 2:
        food = int(input("1 Chicken biryani, 2 Chicken curry, 3 Fish fry: "))
        match food:
            case 1:
                print("Chicken biryani")
            case 2:
                print("Chicken curry")
            case 3:
                print("Fish fry")
            case _:
                print("Invalid food choice")
    case _:
        print("Invalid category")

# Q20
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
match operator:
    case "+":
        print("Result =", num1 + num2)
    case "-":
        print("Result =", num1 - num2)
    case "*":
        print("Result =", num1 * num2)
    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print("Result =", num1 / num2)
    case _:
        print("Invalid operator")

# Q21
choice = int(input("1 Celsius to fahrenheit, 2 Fahrenheit to celsius: "))
temperature = float(input("Enter temperature: "))
match choice:
    case 1:
        print("Temperature =", (temperature * 9 / 5) + 32, "F")
    case 2:
        print("Temperature =", (temperature - 32) * 5 / 9, "C")
    case _:
        print("Invalid choice")

# Q22
choice = int(input("Enter choice: "))
value = float(input("Enter value: "))

match choice:
    case 1:
        print(value * 1000, "meters")
    case 2:
        print(value / 1000, "kilometers")
    case 3:
        print(value * 1000, "grams")
    case 4:
        print(value / 1000, "kilograms")
    case _:
        print("Invalid choice")


# Q23
account = int(input("Enter account type: "))
match account:
    case 1:
        print("Savings account")
    case 2:
        print("Current account")
    case _:
        print("Invalid account")
        exit()

amount = float(input("Enter amount: "))

if amount > 0:
    print("Withdrawal request accepted")
else:
    print("Invalid amount")


# Q24
choice = int(input("Enter choice: "))
match choice:
    case 1:
        age = int(input("Enter age: "))
        if age >= 18:
            print("You can start the exam")
        else:
            print("You cannot start the exam")
    case 2:
        print(" Result")
    case 3:
        print("Exiting Portal")
    case _:
        print("Invalid Choice")


# Q25
choice = int(input("Enter ticket type: "))
age = int(input("Enter age: "))
if age < 5:
    print("Free entry")
else:
    match choice:
        case 1:
            print("Regular ticket")
        case 2:
            print("Premium ticket")
        case 3:
            print("VIP ticket")
        case _:
            print("Invalid choice")


# Q26
device = int(input("Enter device: "))
match device:
    case 1:
        print("Light controller")
    case 2:
        print("Fan controller ")
    case 3:
        print("AC controller")
    case 4:
        print("TV controller")
    case _:
        print("Invalid device")


# Q27
choice = int(input("Enter department: "))
match choice:
    case 1:
        print("General medicine")
    case 2:
        print("Cardiology")
    case 3:
        print("Orthopedics")
    case 4:
        print("Pediatrics")
    case 5:
        print("Emergency")
    case _:
        print("Invalid department")


# Q28
choice = int(input("Enter choice: "))
match choice:
    case 1:
        print("Book ticket")
    case 2:
        print("Cancel ricket")
    case 3:
        print("Check PNR")
    case 4:
        print("Display train schedule")
    case 5:
        print("Exit railway system")
    case _:
        print("Invalid choice")


# Q29
choice = int(input("Enter choice: "))
match choice:
    case 1:
        print("Search book")
    case 2:
        print("Issue book")
    case 3:
        print("Return book")
    case 4:
        print("Issued books")
    case 5:
        print("Exit library system")
    case _:
        print("Invalid choice")


# Q30
status = input("Enter status: ").lower()
match status:
    case "placed":
        print("Your order has been placed")
    case "confirmed":
        print("Your order has been confirmed")
    case "preparing":
        print("Your order is being prepared")
    case "out_for_delivery":
        print("Your order is on the way")
    case "delivered":
        print("Your order has been delivered")
    case "cancelled":
        print("Your order has been cancelled")
    case _:
        print("Invalid order status")


# Q31
banking_type = int(input("Enter banking type: "))
match banking_type:
    case 1:
        print("Personal Banking")
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Personal balance")
            case 2:
                print("Personal transfer")
            case 3:
                print("Personal loan")
            case _:
                print("Invalid option")
    case 2:
        print("Business banking")
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Business balance")
            case 2:
                print("Payroll")
            case 3:
                print("Business loan ")
            case _:
                print("Invalid option")
    case _:
        print("Invalid banking type")


# Q32
role = int(input("Enter role: "))
match role:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Marks")
            case 2:
                print("Attendance")
            case 3:
                print("Homework")
            case _:
                print("Invalid option")
    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Entering marks")
            case 2:
                print("Managing attendance")
            case 3:
                print("Assigning homework")
            case _:
                print("Invalid option")
    case 3:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Child marks")
            case 2:
                print("Child attendance")
            case 3:
                print("Contact teacher")
            case _:
                print("Invalid option")
    case _:
        print("Invalid Role")


# Q33
transport = int(input("Select transport: "))
match transport:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Economy flight")
            case 2:
                print("Business flight")
            case _:
                print("Invalid option")
    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Sleeper train")
            case 2:
                print("AC train")
            case _:
                print("Invalid option")
    case 3:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Ordinary bus")
            case 2:
                print("Volvo bus")
            case _:
                print("Invalid option")
    case _:
        print("Invalid transport")


# Q34
choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Start game")
    case 2:
        print("Load game")
    case 3:
        print("Settings")
        option = int(input("Enter settings: "))
        match option:
            case 1:
                print("Sound")
            case 2:
                print("Graphics")
            case 3:
                print("Controls")
            case _:
                print("Invalid setting")
    case 4:
        print("Exit game")
    case _:
        print("Invalid choice")


# Q35
category = int(input("Select category: "))
match category:
    case 1:
        print("1. Soup")
        print("2. Spring Roll")
        print("3. Garlic Bread")
        item = int(input("Select item: "))
        match item:
            case 1:
                print("Soup")
            case 2:
                print("Spring roll")
            case 3:
                print("Garlic bread")
            case _:
                print("Invalid item")
    case 2:
        print("1. Pizza")
        print("2. Pasta")
        print("3. Biryani")
        item = int(input("Select item: "))
        match item:
            case 1:
                print("Pizza")
            case 2:
                print("Pasta")
            case 3:
                print("Biryani")
            case _:
                print("Invalid item")
    case 3:
        print("1. Ice cream")
        print("2. Cake")
        print("3. Gulab jamun")
        item = int(input("Select item: "))
        match item:
            case 1:
                print("Ice cream")
            case 2:
                print("Cake")
            case 3:
                print("Gulab jamun")
            case _:
                print("Invalid item")
    case 4:
        print("1. Coffee")
        print("2. Tea")
        print("3. Juice")
        item = int(input("Select item: "))
        match item:
            case 1:
                print("Coffee")
            case 2:
                print("Tea")
            case 3:
                print("Juice")
            case _:
                print("Invalid item")
    case _:
        print("Invalid category")


# Q36
payment = int(input("Select payment type: "))
match payment:
    case 1:
        option = int(input("1. Scan QR\n2. Enter UPI ID\nEnter option: "))
        match option:
            case 1:
                print("Scan QR")
            case 2:
                print("Enter UPI ID")
            case _:
                print("Invalid option")
    case 2:
        option = int(input("1. Credit Card\n2. Debit Card\nEnter option: "))
        match option:
            case 1:
                print("Credit card")
            case 2:
                print("Debit card")
            case _:
                print("Invalid option")
    case 3:
        option = int(input("1. Add Money\n2. Pay Using Wallet\nEnter option: "))
        match option:
            case 1:
                print("Add money")
            case 2:
                print("Pay using wallet")
            case _:
                print("Invalid option")
    case _:
        print("Invalid payment type")


# Q37
subject = int(input("Select subject: "))
match subject:
    case 1:
        option = int(input("1. Python\n2. Java\n3. C++\nEnter option: "))
        match option:
            case 1:
                print("Python course")
            case 2:
                print("Java course")
            case 3:
                print("C++ course")
            case _:
                print("Invalid option")
    case 2:
        option = int(input("1. Algebra\n2. Calculus\n3. Statistics\nEnter option: "))
        match option:
            case 1:
                print("Algebra")
            case 2:
                print("Calculus")
            case 3:
                print("Statistics")
            case _:
                print("Invalid option")
    case 3:
        option = int(input("1. English\n2. Presentation\n3. Interview Skills\nEnter option: "))
        match option:
            case 1:
                print("English")
            case 2:
                print("Presentation")
            case 3:
                print("Interview skills")
            case _:
                print("Invalid option")
    case _:
        print("Invalid Subject")


# Q38
choice = int(input("Select option: "))
match choice:
    case 1:
        option = int(input("1. Start\n2. Stop\nEnter option: "))
        match option:
            case 1:
                print("Engine started")
            case 2:
                print("Engine stopped")
            case _:
                print("Invalid option")
    case 2:
        option = int(input("1. Headlights\n2. Indicators\n3. Hazard Lights\nEnter option: "))
        match option:
            case 1:
                print("Headlights")
            case 2:
                print("Indicators")
            case 3:
                print("Hazard lights")
            case _:
                print("Invalid option")
    case 3:
        option = int(input("1. Play\n2. Pause\n3. Next\n4. Previous\nEnter option: "))
        match option:
            case 1:
                print("Play music")
            case 2:
                print("Music pause")
            case 3:
                print("Next track")
            case 4:
                print("Previous track")
            case _:
                print("Invalid option")
    case 4:
        option = int(input("1. Start Navigation\n2. Stop Navigation\nEnter option: "))
        match option:
            case 1:
                print("Navigation started")
            case 2:
                print("Navigation stopped")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid Choice")


# Q39
role = int(input("Enter role: "))

match role:
    case 1:
        option = int(input("1. View Profile\n2. Apply Leave\n3. View Salary\nEnter option: "))
        match option:
            case 1:
                print("Profile")
            case 2:
                days = int(input("Enter leave days: "))
                if days > 0:
                    print("Leave request submitted")
                else:
                    print("Invalid leave days")
            case 3:
                print("View Salary")
            case _:
                print("Invalid option")
    case 2:
        option = int(input("1. View Team\n2. Approve Leave\n3. View Reports\nEnter option: "))
        match option:
            case 1:
                print("View team")
            case 2:
                print("Approve leave")
            case 3:
                print("View reports")
            case _:
                print("Invalid option")
    case _:
        print("Invalid Role")


#Q40
role = int(input("Enter role: "))
match role:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Student profile")
            case 2:
                print("Student marks")
            case 3:
                print("Student attendance")
            case 4:
                print("Courses")
            case _:
                print("Invalid choice")
    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Students")
            case 2:
                print("enter Marks")
            case 3:
                print("attendance")
            case 4:
                print("Courses")
            case _:
                print("Invalid choice")
    case 3:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Fees")
            case 2:
                print("Admissions")
            case 3:
                print("Notices")
            case 4:
                print("Departments")
            case _:
                print("Invalid choice")
    case _:
        print("Invalid choice")