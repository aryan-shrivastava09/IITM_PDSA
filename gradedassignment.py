def issymmetricBad(L):
    try:
        while len(L) > 0:
            if L.pop(0) != L.pop(-1):
                return False
            return True
    except IndexError:
        print('IndexError')
    except:
        print('Some other exception occurred')
    else:
        print('No exception occurred')
L = [2,4,6] 
issymmetricBad(L)