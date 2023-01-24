def quicksort(L,l,r):   
    if (r-l<=1):
        return L
    pivot, lower, upper = L[0], l+1,l+1
    for i in range(l+1,r):
        if L[i] > pivot:
            upper +=1
        else:
            L[i],L[lower] = L[lower] , L[i]
            lower, upper = lower+1, upper+1
    
    L[lower-1], L[l] = L[l] , L[lower-1]
    lower -=1

    quicksort(L,l,lower)
    quicksort(L,lower+1,upper)

    return L

L = [10,12,1,8,4]
print(quicksort(L,0,len(L)))