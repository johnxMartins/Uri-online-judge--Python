# -*- coding: utf-8 -*-
peca1=input()
A,B,C=peca1.split()
D=int(B)
E=float(C)
peca2=input()
F,G,H=peca2.split()
I=int(G)
J=float(H)
print("VALOR A PAGAR: R$ %.2f"%(D*E+I*J))