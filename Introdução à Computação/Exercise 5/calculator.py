num1 = int(input("First number: "))
num2 = int(input("Second number: "))
command = ""


def add():
    res = num1 + num2
    return res

def sub():
    res = num1 - num2
    return res

def mul():    
    res = num1 * num2
    return res

def div():
    res = num1 / num2
    return res

def pri():
    numPrim = int(input("See if this number is prime: "))
    if numPrim > 1:
        for i in range(2, numPrim):
            if (numPrim % i) == 0:
                print("This is not a prime number")
    else:
        print("This is a prime number")


def cal():
    command = input("Choose your operation add/sub/mul/div (exit to break): ")

    if command == "add":
        print("The result is: " + str(add()))
    elif command == "sub":
        print("The result is: " + str(sub()))
    elif command == "mul":
        print("The result is: " + str(mul()))
    elif command == "div":
        print("The result is: " + str(div()))
    else:
        print("Select a corret operation!")
        cal()

cal()
pri()
