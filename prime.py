def factors(m):
    f = []
    for i in range(1,m+1):
        if m%i==0:
            f.append(i)
    return f

def prime(n):
    if len(factors(n)) == 2:
        return True
    return False

n = int(input("Enter a number: "))
print(prime(n))