n = int (input ("Write a number: "))

factorial = 1

if n >= 1:

    for i in range (1, n + 1):

        factorial = factorial * i

print ("The factorial of the number is: " + str(factorial))