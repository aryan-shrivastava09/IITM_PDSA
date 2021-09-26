import itertools

def findsubsets(L,P):
    L = L.split(" ")
    L = [int(n) for n in L]
    return list(itertools.combinations(L,P))

def find_Min_Difference(L,P):
    subsets = findsubsets(L,P)
    diff_list = []
    for t in subsets:
        d = max(t) - min(t)
        diff_list.append(d)
    return min(diff_list)

    
L=((input("Enter List Elements: ")).strip())
P=int(input("Enter Subset size: "))
print(find_Min_Difference(L,P))