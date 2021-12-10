X = int(input())
Y = int(input())
soma=0
if (Y>X):
    for a in range(X,(Y+1)):
        if (a%13!=0):
            soma+=a
if (X>Y):
    for a in range(Y,(X+1)):
        if (a%13!=0):
            soma+=a
print(soma)