import matplotlib as mpl
import matplotlib.pylab as plt
import numpy as np

#matplotlib:Figure,Axis,Axes객체로 구성
#Figure는 1개 이상의 Axes로 구성
# f1 = plt.figure(figsize=(10,2)) #그림의 크기
# plt.plot(np.random.randn(100))

# f1 = plt.figure(1)
# plt.plot([1,2,3,4],'ro:')
# f2 = plt.gcf() #기존의 plot의 figure를 그대로 복사해 온다
# print(f1,id(f1))
# print(f2,id(f2)) #f2 = plt.gcf()에 의해 f1과 같은 것이 복사
# plt.show()

#화면 나누기(subplot)
x1 = np.linspace(0.0,5.0)
print(x1)
x2 = np.linspace(0.0,2.0)
y1 = np.cos(2*np.pi*x1)*np.exp(-x1)
y2 = np.cos(2*np.pi*x2)

ax1 = plt.subplot(2,1,1)
plt.plot(x1,y1,'yo-')

ax2 = plt.subplot(2,1,2)
plt.plot(x2,y2,'r.-')
plt.show()
