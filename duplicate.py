L = [12,54,68,759,24,15,12,68,987,758,25,69]
from collections import Counter
def find_duplicates(L):
    if len(set(L)) == len(L):
        return L
    c = Counter(L)
    return find_duplicates([key for key in c if c[key]>1])

l = find_duplicates(L)
print(l)

# d = {
#     1 : 4,
#     2 : 8,
#     3 : 7
# }
# for (key,value) in d.items():
#     print(key,value)