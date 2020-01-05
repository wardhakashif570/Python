#FV = I * [1 + (R * T)] future value formula
amount =int(input(" Enter a amount"))
interest =int(input(" Enter a rate of intrest "))
year =int(input(" Enter a year "))
result = amount * [1 + (interest * year)]
print("the future value of a specified principal amount is " + str(result))
