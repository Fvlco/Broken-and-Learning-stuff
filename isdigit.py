# .isdigit() -> character check 0-9 -> true or else "-5"/"3.5" -> false.
# Validation check

NUMERO = input("Enter a number ya filthy casual: ").strip()

while NUMERO.isdigit() != True: 
    print("Nice try, lets try again. Type your IQ number.")
    NUMERO = input("ENTER WHOLE NUMBER: ").strip()

NUMERO = int(NUMERO)
print(f"Valid Number {NUMERO}")

#pro tip: while not NUMERO.isdigit():
