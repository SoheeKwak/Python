class MulLayer:
    def __inti__(self):
        self.x = None #초기화 상태에서는 아직 값을 지정해 주지 않음
        self.y = None
    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x*y
        return out
    def backward(self, dout):#dout에 1전달
        dx = dout*self.y
        dy = dout * self.x
        return dx,dy #dapple_price, dtax

apple = 100
apple_num = 2
tax = 1.1

# 2개의 계층 신경망
mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

#forward propagation
apple_price = mul_apple_layer.forward(apple, apple_num)
price = mul_tax_layer.forward(apple_price, tax)

#backward propagation
dprice = 1
dapple_price, dtax = mul_tax_layer.backward(dprice) #1.1, 200
dapple, dapple_num= mul_apple_layer.backward(dapple_price)
print("price:",int(price))
print("dApple",dapple)
print("dApple_num:", int(dapple_num))
print("dTax:", int(dtax))