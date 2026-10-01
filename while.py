name = input("Enter your name: ").strip()

while name == "":
    print("Name cannot be empty!")
    name = input("Enter your name: ").strip()
print(name)