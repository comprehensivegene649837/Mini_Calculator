print("****** WELCOME! ******")
print("   ")


a= (float(input("enter the number here: ")))
b= (float(input("enter the number here: ")))

print(" PLEASE SELECT THE OPERATOR THAT YOU WOULD LIKE TO USE: ")
print("1. '*' - for multiplication")
print("2. '+' - for addition")
print("3. '-' - for subtraction")
print("4. '/' - for division")

operator= (input("enter the operator: "))

if operator=="1" or operator=="*":
    print(f"the multiplication of {a} and {b} is {a *b}")

elif operator =="2" or operator==("+"):

    print(f"the addition of {a} and {b} is {a + b}")
elif operator=="3" or operator==("-"):

    print(f"the subtraction of {a} and {b} is {a - b}")
elif operator =="4" or operator==("/"):

    print(f"the divion of {a} and {b} is {a/b}")

else:
    print("invalid input")