for i in range(100, 200):
    res = 0
    for j in str(i):
        res = res + int(j)
    if res % 2 == 0:
        print("Number" + str(i))
  
  
