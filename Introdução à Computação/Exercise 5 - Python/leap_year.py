ano = int(input("Year: "))
if (ano %  4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("It\'s a Leap year")
else:
    print("It\'s not a leap year")