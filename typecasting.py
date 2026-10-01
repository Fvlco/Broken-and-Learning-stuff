# Process of converting a 
# variable from one data type another data type
# str(), int(), float(), bool()

name = "Falco" #string
age = 201 #integer
gpa = 5.2 #float
is_student = True #boolean

print(type(is_student))

# change to another data type

gpa = int(gpa) #rounds down to integer
print(gpa) 

age = str(age) #TYPE CAST

age += "1" #must use "" -> cuz 'age' is now a string data type

print(age)


# BOOLEAN
name = bool(name) 

print(name)

# note: here, if the variable 'name'
# is empty, it returns FALSE only. 
# Use: USER INPUTS. to prompt retyping name