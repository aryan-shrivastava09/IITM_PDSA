def prime(n):
    result, i = True, 2
    for i in range(2,n):
        if (n%i)==0:
            result = False
    return result

n = int(input("Enter a number: "))
print(prime(n))
