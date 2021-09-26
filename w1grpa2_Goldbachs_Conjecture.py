import math
def prime(n):
    if n<=0 or n==1:
        return False
    elif n==2 or n==3:
        return True
    elif n%2==0 or n%3==0:
        return False
    for i in range(5,round(math.sqrt(n))+1, 6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True


def Goldbach(n):
    l = []
    if n%2==0:
        for i in range(1,round(n/2)+1):
            print(i)
            if prime(i) and prime(n-i):
                l.append((i,n-i))
    return l

n=int(input())
print(sorted(Goldbach(n)))