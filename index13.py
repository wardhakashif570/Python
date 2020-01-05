number1 = int(input("Enter a number 1"))
number2 = int(input("Enter a number 2"))
def check(number1,number2):
    if number1 == number2 or number1 + number2 == 5 or number1 - number2 == 5 or number2 - number1 == 5:
        return "true";
print(check(number1,number2))
