def insertionSort(L):
    n = len(L)
    if n<1:
        return L
    for i in range(n):
        j = i
        while(j>0 and L[j]<L[j-1]):
            (L[j],L[j-1]) = (L[j-1], L[j])
            j-=1
    return L