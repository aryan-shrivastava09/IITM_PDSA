def gcd(m,n):
    (a,b) = (max(m,n), min(m,n))
    if a%b==0:
        return b
    else:
        print(1)
        return gcd(b, a%b)
    
print(gcd(24,130))