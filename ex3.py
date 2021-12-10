# -*- coding: utf-8 -*-
A,B=input().split()
c=int(A)
d=int(B)
if c%d==0:
    print("Sao Multiplos")
elif d%c==0:
	print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
