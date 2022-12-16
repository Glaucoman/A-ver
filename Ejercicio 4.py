c=0
while c <= 5:
    c+=1
    if c==3  or c==4:
        #print ("rompemos bucle cuando c vale", c)
        continue
    print ("c vale", c)
else:
    print ("se a completado toda la iteracion y c vale", c)