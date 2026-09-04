name = input("Enter your name: ")
lab = int(input("Enter your lab: "))
product_name = input("Enter the product's name: ")
quantity = int(input("Enter the quantity: "))
price =float(input("Enter the price: "))
total_price = quantity*price


print(f"My name is: {name}""\n"
      f"My lab is: {lab}""\n"
      f"The product name is: {product_name}""\n"
      f"The quantity is: {quantity}""\n"
      f"The price is: {price}""\n"
      f"The total price is: {total_price}""\n"
)
a,b = map(int,input("Enter two numbers: ").split())
print(a,b, type(a), type(b))

a,b = map(int,input("Enter two numbers: ").split()[:2])
print(a,b, type(a), type(b),)

date = input("Enter the date: ")
month = int("09")
year = 2026
print(date, month, year, end=" ")