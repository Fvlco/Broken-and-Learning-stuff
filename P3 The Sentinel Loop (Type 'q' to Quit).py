#The Mission: Write a while True loop that continuously asks the user to enter an item name. 
# If they type "q", print "Exiting order..." and use break to kill the loop. 
# If they type anything else, print "Added to cart!" and loop again.

#making a list:
godown = []
realvalues = []
import time

while True:

    val = input("Enter valid item name (q to exit): ").strip() #Edge case: Whitespace

    if val == "q" or val == "quit" or val == "Quit":          #Grabs into loop if the val is sentinel val("q") otherwise skips this if loop
        print("Stopping...")
        print(f"Here's the lower case {godown}")
        print(f"Here's the original {realvalues}")
        time.sleep(0.5)
        break
    elif val == "":         #Edge case: empty
        print("You did not type anything!")
    elif val.isdigit():     #Edge case: non digits
        print("The item name cannot be digits!")
    else: 
        realvalues.append(val)
        lowercasedval = val.lower()
        godown.append(lowercasedval)
    