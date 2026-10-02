#The Mission: Create a dictionary called menu with at least 3 food items and their prices. 
# Then, write a couple of print statements that look up and print the price of two specific items using their keys.

menu = { #key: value (Not key EQUAL(=) value)
        "burger": "5$",
        "pizza": "10$",
        "noodles": "7$"
}
burgerprice = menu["burger"]
print(f"Price of burger is: {burgerprice}")
import time
time.sleep(.5)
print(menu["noodles"])
