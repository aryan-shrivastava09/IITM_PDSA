def BinarySearch(v,l):
    if l==[]:
        return False
    m = len(l)//2
    if v==l[m]:
        return True
    elif v<l[m]:
        return BinarySearch(v,l[:m])
    else:
        return BinarySearch(v,l[m+1:])