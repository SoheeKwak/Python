def cost_function(x, y, w):
    cost = 0
    for i in range(len(x)):
        hx = w * x[i] # hx함수 = 10 * x
        # print(hx)
        cost+=(hx-y[i])**2 # cost: 오차의 제곱의 합(오차가 클수록 cost가 매우 커짐)
    return cost/len(x)

x = [1,2,3] # 입력값
y = [1,2,3] # 출력값
# y = w(기울기) * x
w = 10
print(cost_function(x,y,w))
print(cost_function(x,y,5))
print(cost_function(x,y,1)) # w(기울기)가 줄어들 수록 오차가 작다는 의미. 즉, cost가 0이 되면 오차가 없다는 의미.
#
xxx, yyy = [], []
for i in range(-50, 50):
    w = i/10  # -5, -4.9, -4.8,............, 4.8, 4.9
    c = cost_function(x,y,w)
    print(w,c)
    xxx.append(w)
    yyy.append(c)

import matplotlib.pyplot as plt
plt.plot(xxx, yyy)
plt.plot(xxx, yyy, 'ro')
plt.show()