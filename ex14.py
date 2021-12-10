N=int(input())
print(N)
while N>0 or N<=1000000:
   Q100 = N // 100
   NR100 = N % 100
   Q50 = NR100 // 50
   NR50 = NR100 % 50
   Q20 = NR50 // 20
   NR20 = NR50 % 20
   Q10 = NR20 // 10
   NR10 = NR20 % 10
   Q5 = NR10 // 5
   NR5 = NR10 % 5
   Q2 = NR5 // 2
   NR2 = NR5 % 2
   Q1 = NR2 // 1
   NR1 = NR2 % 1
   print(Q100,"nota(s) de R$ 100,00")
   print(Q50,"nota(s) de R$ 50,00")
   print(Q20,"nota(s) de R$ 20,00")
   print(Q10,"nota(s) de R$ 10,00")
   print(Q5,"nota(s) de R$ 5,00")
   print(Q2,"nota(s) de R$ 2,00")
   print(Q1,"nota(s) de R$ 1,00")
   break