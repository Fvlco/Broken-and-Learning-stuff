# word = key. definition = value. Hence it's called dictionary


#               1. Creating a Dictionary

user = {
    "username":"this is the key", #strings get []""]
    "level": 5, #comma at all
    "score": 1500, #comma
    "birthdate": "20th May" # NO comma at end
}


#               2. Looking Up a Value (Reading Data)

print(user["score"]) #print(*dictionaryname*["*key*"])
print(user["username"]) 
print(user["level"])
print(user["birthdate"])
import time
time.sleep(1)

#               3. Adding or Changing Data

#Changing existing value
user["level"] = 10
print(user["level"])

time.sleep(.5)


#Add brand new key-value pair
user["is this new"] = "Yes"

print(user["is this new"])


bigcaps = input("CAPITAL LETTER PLEASE (username/level/score/birthdate): ")
smallcaps = bigcaps.lower()
time.sleep(.5)

if smallcaps in user:
    davalue = user[smallcaps]
    print(f"The value of {smallcaps} is {davalue}")




