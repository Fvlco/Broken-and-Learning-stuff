

listname = ["Item1", "Apple", "Banana"] # name = ["x","y","z"]

#Manually add
listname.append("Number")
listname.append("5")

print(listname)

import time
time.sleep(0.5)
useradd = input("Enter a list name: ").strip()

listname.append(useradd)
print(listname)
