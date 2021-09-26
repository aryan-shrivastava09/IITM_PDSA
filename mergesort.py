def merge(A,B):
    m,n = len(A), len(B)
    (C,i,j,k) = ([],0,0,0)
    while k<m+n:
        if i==m:
            C.extend(B)
            k+=(n-j)
        elif j==n:
            C.extend(A)
            k+=(n-i)
        elif A[i]<B[j]:
            C.append(A[i])
            (i,k)=(i+1,k+1)
        else:
            C.append(B[j])
            (j,k) = (j+1,k+1)
    return C

def mergesort(A):
    n = len(A)
    if n<=1:
        return A
    L = mergesort(A[:n//2])
    R = mergesort(A[n//2:])

    B = merge(L,R)
    return B
    