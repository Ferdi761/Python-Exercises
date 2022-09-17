print("simple arithmetic\n")
print("1. plus (+)")
print("2. minus (-)")
print("3. times (*)")
print("4. divide (/)")
print("5. modulo (%)\n")

num1 = float(input("-> input your first number: "))
num2 = float(input("-> input your second number: "))
opInput = input("-> input your arithmetic operator: ")

if (opInput == "1" or opInput == "+"):
    res = num1 + num2
    print("the result is: ", res)
elif (opInput == "2" or opInput == "-"):
    res = num1 - num2
    print("the result is: ", res)
elif (opInput == "3" or opInput == "*"):
    res = num1 * num2
    print("the result is: ", res)
elif (opInput == "4" or opInput == "/"):
    res = num1 / num2
    print("the result is: ", res)
elif (opInput == "5" or opInput == "%"):
    res = num1 % num2
    print("the result is: ", res)
else:
    print("error: invalid operator!")
