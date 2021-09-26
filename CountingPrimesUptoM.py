import math
def prime(n):
    result, i= True, 2
    while (result and i<math.sqrt(n)):
        if n %i==0:
            result = False
        i+=1
    return result

def countingPrimes(m):
    p1 = []
    for i in range(1,m+1):
        if prime(i):
            p1.append(i)
    print(p1)

print(countingPrimes(100))
