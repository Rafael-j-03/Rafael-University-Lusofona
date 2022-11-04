nmax = int(input("What's your max number for the sequence? "))

n1 = 0
n2 = 1

if nmax == 0 or 1:
   print("Fibonacci sequence up to " + str(nmax))

elif nmax > 0:
    while nmax >= n1:
     print(n1)
     nth = n1 + n2
     #Update dos valores
     n1 = n2
     n2 = nth

else:
    print ("Choose a positive number!")

    