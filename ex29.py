data=input().split()
a=int(data[0])
b=int(data[1])
div=divmod(a,abs(b))
if b<0 :
    print(-div[0],div[1])
else :
    print(div[0],div[1])