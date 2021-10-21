def type_to_string(t):
    if type(1) is t:
        return 'int'
    elif type(1.5) is t:
        return 'float'
    elif type('Aryan') is t:
        return 'str'
    elif type(False) is t:
        return 'bool'

def odd_one(L):
    flag = type(L[0])
    for i in range(1, len(L)-1):
        if type(L[i]) is not flag:
            if type(L[i+1]) is flag:
                text = type_to_string(type(L[i]))
                return text
            else:
                text = type_to_string(type(L[0]))
                return text
    text = type_to_string(type(L[-1]))
    return text


print(odd_one(eval(input().strip())))