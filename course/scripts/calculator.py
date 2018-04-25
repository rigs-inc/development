# Calculator Requirements

# Sum
def sum(number1, number2):
    return number1 + number2

# Rest
def rest(number1, number2):
    return number1 - number2

# Multiply
def multiply(number1, number2):
    return number1 * number2

# Divide
def divide(number1, number2):
    return number1 / number2


print "Welcome User, you can perform:"
print "- For sum press 1"
print "- For rest press 2"
print "- For multiply press 3"
print "- For divide press 4"

operation = input("Which operation do u want to perform?: ")
number1 = input("Input number 1: ")
number2 = input("Input number 2: ")

if operation == 1:
    result = sum(number1, number2)
elif operation == 2:
    result = rest(number1, number2)
elif operation == 3:
    result = multiply(number1, number2)
elif operation == 4:
    result = divide(number1, number2)
else:
    result = "Unknown operation"

print ""
print "**** RESULT ****"
print result
