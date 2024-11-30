name = input("enter your first name: ")
surname = input("enter your last name: ")
age = int(input("enter your age: "))
come_from = input("enter where are you from: ")
if age == 1:
    print(f"Your full name is {surname} {name}. You're {age} year old and you are from {come_from}. Your are a baby")
if 18 > age > 1:
    print(f"Your full name is {surname} {name}. You're {age} years old and you are from {come_from}. You are a teenager")
if age >= 18:
    print(f"Your full name is {surname} {name}. You're {age} years old and you are from {come_from}. You are an adult")


