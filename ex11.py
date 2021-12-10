# -*- coding: utf-8 -*-
A,B,C=input().split()
MaiorAB=(int(A)+int(B)+abs(int(A)-int(B)))/2
MaiorABC=(MaiorAB+float(C)+abs(MaiorAB-float(C)))/2
print("%d eh o maior"%MaiorABC)