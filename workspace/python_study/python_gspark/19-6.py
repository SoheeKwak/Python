import matplotlib as mpl
import matplotlib.pylab as plt
import numpy as np

plt.title('Plot')
# plt.plot([10,20,30,40],[1,4,9,16],'rs--') # rs--: red square 점선
# plt.show()
# plt.plot([10,20,30,40],[1,4,9,16],'bo--') # blue circle
# plt.show()
# plt.plot([10,20,30,40],[1,4,9,16],'bD--') # blue Diamond
# plt.show()
# plt.plot([10,20,30,40],[1,4,9,16],'bD-.')
# plt.xlim(0.50)
# plt.ylim(-10,30)
x = np.linspace(-np.pi, np.pi,256)
c = np.cos(x)
# plt.plot(x,c)
# plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
#            ['a','b','c','d','e'])
# plt.yticks([-1,0,1],['low','zero','high'])
# plt.show()


# t = np.arange(0.,5.,0.2)
# plt.plot(t,t,'r--',t,0.5*t**2, 'bs:',t,0.2*t**3,'g^-')
# plt.show()

x = np.linspace(-np.pi, np.pi,256)
c,s = np.cos(x),np.sin(x)
plt.plot(x,c,ls="--",label="cosine")
plt.plot(x,s,ls=":",label="sine")
# plt.legend() #디폴트(loc=0,best)가장 적절한 위치에 범례 출력
plt.legend(loc=1) #loc=0~10
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.show()

