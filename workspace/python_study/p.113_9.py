money, c50000, c10000, c5000, c1000, c500, c100, c50, c10 = [0] * 9

money = int(input("교환할 돈은 얼마?"))

c50000 = money // 50000
money %= 50000

c10000 = money // 10000
money %= 10000

c5000 = money //5000
money %=5000

c1000 = money //1000
money %=1000

c500 = money //500
money %=500

c100 = money //100
money %=100

c50 = money //50
money %=50

c10 = money //10
money %=10

print("5만원 %d장" % c50000)
print("1만원 %d장" % c10000)
print("5천원 %d장" % c5000)
print("1천원 %d장" % c1000)
print("5백원 %d개" % c500)
print("1백원 %d개" % c100)
print("50원 %d개" % c50)
print("10원 %d개" % c10)
