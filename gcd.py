mrcf = 1
def gcd(m,n):
    for i in range(1, min(m,n)):
        if (m%i)==0 and (n%i) == 0:
            mrcf = i
    return mrcf

print(gcd(50,60))
