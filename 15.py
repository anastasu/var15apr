for A in range(1000,1,-1):
    OK = 1
    for x in range(0,100):
        for y in range(0,100):
            OK *= ((x*y < 100) or (y>=A) or (x>A))
    if OK:
        print(A)
        break


