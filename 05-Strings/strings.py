#Task 1
name = "Neel",'Neel'
age = "17",'17'
fav_prog_language = "Python",'Python'
text = "Welcome",'Welcome'

print(name)
print(age)
print(fav_prog_language)
print(text)

#Task 2
text = ""

print(text)
print(len(text))
print(type(text))

#Task 3
text = "Python Programming"

print(text)
print(len(text))
print(text[len(text)-18])
print(text[len(text)-1])
print(text[len(text)-16])
print(text[len(text)-2])

#Task 4
text = "Programming"

print(text[0])
print(text[1])
print(text[4])
print(text[10])

#Task 5
print(text[-1])
print(text[-2])
print(text[-3])
print(text[-11])

#Task 6
name = "Neel Parmar"

print(name[0])
print(name[-1])
print(name[5])

#Task 7
text = "Python Programming"

print(len(text))
print(text[0:6])
print(text[7:])
print(text[:])
print(text[:6])
print(text[13:])

#Task 8
text = "ABCDEFGHIJKL"

print(text[1::2])
print(text[2::3])
print(text[1:8:2])
print(text[::-1])

#Task 9
text = "Python Programming"

print(text[-5:])
print(text[-10:])
print(text[::-1])

#Task 10
text = "Dictionary"

print(text[:3])
print(text[-3:])
print(text[1::2])
print(text[::-1])
print(text[1:9])

#Task 11
str_1 = "CSS"
str_2 = "The sun sets."
str_3 = "The blue bicycle rolled down the steep hill before stopping near the old red barn."

print(len(str_1))
print(len(str_2))
print(len(str_3))

#Task 12
text = "Python Programming"
last_index = len(text)-1

print(len(text))
print(last_index)
print(text[last_index])

#Task 13
first_name = "Neel"
last_name = "Parmar"
full_name = "Neel"+" "+"Parmar"

print(full_name)

#Task 14
name = "Jitesh "
age = str(19)
city = "Mumbai "
prog_language = "Python "
sentence = name+"is "+age+" "+"year-old "+prog_language +"developer "+"from "+ city

print(sentence)

#Task 15
name = "Rahul "
age=str(17)

print(name+age)

#Task 16
string = "Hello World "

print(string*3)
print(string*5)
print(string*10)

#Task 17
symbol = "*"

print(symbol*10)

#Task 18
text = "python programming language"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())

#Task 19
str_1 = "Python"
str_2 = "python"

print(str_1==str_2)

str_1=str_1.lower()
str_2=str_2.lower()

print(str_1==str_2)

#Task 20
sentence = "Python is a programming language"

print("Python" in sentence)
print("programming" in sentence)
print("Java" in sentence)
print("language" in sentence)

#Task 21
print(sentence.find("Python"))
print(sentence.find("programming"))
print(sentence.find("language"))
print(sentence.find("Java")) # returns -1

#Task 22
# print(sentence.index("Java")) # returns error

#Task 23
text = "banana"

print(text.count("a"))
print(text.count("n"))
print(text.count("b"))

#Task 24
filename = "student_notes.pdf"

print(filename.startswith("student"))
print(filename.endswith(".pdf"))
print(filename.endswith(".txt"))

#Task 25
text = "I am learning Java"
new_text=text.replace("Java","Python")

print(new_text)

#Task 26
text = "apple apple apple"

print(text.replace("apple", "mango"))

#Task 27
print(text.replace("apple", "mango", 1))

#Task 28
text = "Python"
text.upper()

print(text)

text=text.upper()

print(text)

#Task 29
text = "   Python Programming   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())

#Task 30
name = input("Enter your name: ")
name = name.strip()

print(name)

#Task 31
text = "Python is easy to learn"
words = text.split()

print(words)

#Task 32
text = "apple,banana,mango,orange"
words = text.split(",")

print(words)

#Task 33
words = ["Python", "is", "easy"]
join= " ".join(words)

print(join)

#Task 34
list = ["Python", "is", "easy"]
join="-".join(list)

print(join)

list = ["Python", "is", "easy"]
join="/".join(list)

print(join)

#Task 35
name = "Krish"
age = 21
city = "Ahmedabad"

print(f"My name is {name} and I am {age} years old. I live in {city}.")

#Task 36
a = 10
b = 20

print(f"The sum is {a+b}")

#Task 37
# (A) text = "Python"
# print(text[20]) #TypeError
text = "Python"

print(text[:])

# (B) text = "Python"
# text[0] = "J" #TypeError
text = "Python"

print("J"+text[1:])

# (C) age = 20
# print("Age: " + age) #TypeError
age = str(20)

print("Age: " + age)

# (D) text = "Python"
# print(text.index("Java")) #ValueError
text = "Python"

print(text.find("Java"))


#Task 38
user_name = input("Enter your name: ")

print(user_name)

user_name = user_name.strip()

print(user_name)
print(user_name.upper())
print(user_name.lower())
print(user_name.title())
print(len(user_name))
print(user_name[0])
print(user_name[-1])

character = input("Enter a character to check: ")

print(character in user_name)


#Task 39
sentence=input("Type something: ")

print(sentence)
print(len(sentence))
print(len(sentence.split()))
print(sentence[0])
print(sentence[-1])
print(sentence.upper())
print(sentence.lower())
print(sentence.title())
print("Python" in sentence)

character=input("Enter a character to check how many times it occured: ")

print(sentence.count(character))

#Task 40
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
city = input("Enter your city: ")
course = input("Enter your course name: ")
age = input("Enter your age: ")

first_name = first_name.strip()
last_name = last_name.strip()
city = city.strip()
course = course.strip()
age = age.strip()
full_name = first_name+" "+last_name

print(full_name.title())
print(full_name.upper())
print(full_name.lower())
print(len(full_name))
print(full_name[0])
print(full_name[-1])
print(city,course)
print(f"{full_name} is {age} years old")
print("Python" in course)

old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

print(course.replace(old_word, new_word))
print(len(course.split()))
