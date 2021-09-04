def prime(n):
    (result,count) = (True,0)
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count!=2:
        result = False
    return result

n = int(input("enter a number: "))
print(prime(n))

