# or and not


temperature = int(input("Enter the temperature in celcius: "))
is_raining = False


if temperature > 35 or temperature < 0 or is_raining: #HOT | FREEZING | RAINING
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still ongoing")





# AND
temp = 25
is_SUNNY = True

if temp >=28 and is_SUNNY:
    print("It is HOT outside")
else:
    print("It is Sunny")

