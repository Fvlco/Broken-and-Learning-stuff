# if,elif,else

age = int(input("Enter your age: "))
has_ticket = False
price = 10.00

if 18 <= age <= 25:
    print("You are an adult")
    print(f"Ticket price for an adult is ${price * .75}")
elif 25 < age <= 40:
    print("You are middle aged") 
    print(f"Price for middle aged citizens is ${price * 0.70}")
elif 40 < age < 65:
    print("You are aging older")
    print(f"Price for aging citizens is ${price * 0.65}")
elif 65 <= age <= 130:
    print("You are a senior citizen")
    print(f"Price for senior citizen is ${price * 0.5}")
elif age < 0:
    print("You haven't been born yet")
elif age ==0:
    print("You were just born")
elif 0 < age <= 11:
    print("You are a toddler")
    print(f"Price for a toddler is ${price * 0.5}")
elif 12 <= age < 18:
    print("You are a teen")
    print(f"Price for a teen is ${price * 0.55}")
else: 
    print("You are fucking dead")

if has_ticket:
        print("You may enter, you have a ticket")
else:  
        print("YOU SHALL NOT PASS")






