import numpy as np

def AND(x1, x2): #AND 게이트 00 01 10 11 => 0 0 0 1
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x)+b
    if tmp <=0:  #w1*x1 + w2*x2 <=0
        return 0
    else:        #w1*x1 + w2*x2 >0
        return 1


def NAND(x1, x2): #NAND 게이트 00 01 10 11 => 1 1 1 0
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x)+b
    if tmp <=0:  #w1*x1 + w2*x2 <=0
        return 0
    else:        #w1*x1 + w2*x2 >0
        return 1


def OR(x1, x2): #NAND 게이트 00 01 10 11 => 0 1 1 1
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x)+b
    if tmp <=0:  #w1*x1 + w2*x2 <=0
        return 0
    else:        #w1*x1 + w2*x2 >0
        return 1

def XOR(x1, x2):#00 01 10 11 => 0 1 1 0 (배타적 논리의 합)
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

if __name__ == '__main__':
    for xs in [(0,0),(0,1),(1,0),(1,1)]:
        y = XOR(xs[0], xs[1])
        print(str(xs)+"->"+str(y))