import math
def prime(n):
    result, i = True, 2
    while (result and i<math.sqrt(n)):
        if (n%i)==0:
            result = False
        i+=1
    return result

n = int(input("Enter a number: "))
print(prime(n))