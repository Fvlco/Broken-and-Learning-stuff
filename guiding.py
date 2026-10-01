name = input("Enter your name: ").strip()
while name == "":
    print("Name cannot be empty!")
    name = input("Enter your name: ").strip()
    

age = int(input(f"Hello {name}! Enter your age please!: ").strip())


while age > 120 or age <= 0:
    if age <= 0:
        print("Age cannot be zero or less!")
    else:
        print("Fossil Fuel?💀")
    age = int(input(f"I'm not playing bro, enter your AGE: ").strip())

print(f"Hello {name}! You are {age} years old!")
