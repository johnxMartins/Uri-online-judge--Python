def primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

rep = int(input())

for i in range(rep):
    num = int(input())
    if primo(num) == True:
        print("%d eh primo"% num)
    else:
        print("%d nao eh primo"% num)