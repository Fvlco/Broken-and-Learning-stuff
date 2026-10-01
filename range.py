#range(start, stop, step) - aoe <- sta, sto, ste.
#Stop is exclusive, meaning upto 1 number below target stop. 
#Start is inclusive. It is included and counted.


#Repeat an Action a Specific Number of Times (Simplest Use)
for i in range(1): # [Repeats 3 times. 3-> stop val.AUTO: 0-> start val. 1-> Step val]
    print("Basic repeats!")


#Specifying a Custom Starting Point (start and stop)
for i in range(1,9): #Starts from 5 upto 8, exclude 9. Steps +1 [ START. STOP ]
    print("1-9, prints 8 times, excluding 9 and includes 1") #Counts from 5, as start-> inclusive. 5,6,7,8. Stops counting at 8th, cuz 9 is stop val and exclusive


#Skipping Numbers (start, stop, and step)
for i in range(2, 10, 2): #Starts from 2, upto 9 excludes 10. And 2 skips at a time, so won't reach 9
    print(i)


#Counting Backwards (Negative step)
#If your step is negative, your start must be higher than your stop. Python will subtract from the counter instead of adding.
#repeat(x,y,-z) -> x > y

for i in range(10,2,-1):
    print(i)