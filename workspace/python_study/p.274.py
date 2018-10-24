list1=[1, 2, 3, 4]
list2=[10, 20, 30, 40]

def hapfunc(n1, n2) :
    return n1+n2

haplist = list(map(hapfunc, list1, list2))
print(haplist)