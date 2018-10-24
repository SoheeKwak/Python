##영상 처리 및 데이터 분석 툴
from tkinter import *
from tkinter.filedialog import *
import os.path
import math
from tkinter.simpledialog import *

##함수 선언부
def loadImage(fname):
    global window, canvas, paper, filename, inImageR, inImageG, inImageB, outImageR, outImageG,outImageB, inW, inH, outW, outH, photo
    photo = PhotoImage(file=filename)
    inW = photo.width()
    inH = photo.height()
    inImageR, inImageG, inImageB = [],[],[]
    tmpLIst = []
    for i in range(inH): #입력메모리 확보(0)으로 초기화
        tmpLIst =[]
        for k in range(inW):
            tmpLIst.append(0)
            inImageR.append(tmpLIst[:])
            inImageG.append(tmpLIst[:])
            inImageB.append(tmpLIst[:])
    #파일--> 메모리로 데이터 로딩
    for i in range(inH):
        for k in range(inW):
            r,g,b = photo.get(k,i)
            inImageR[i][k] = r
            inImageG[i][k] = g
            inImageB[i][k] = b
    photo = None

def openFile():
    global window, canvas, paper, filename, inImageR, inImageG, inImageB, outImageR, outImageG,outImageB, inW, inH, outW, outH
    filename = askopenfilename(parent=window,
                               filetypes=(("GIF파일", "*.gif"), ("모든파일", "*.*")))
    loadImage(filename) #파일 -->입력메모리
    equal() #입력 메모리-->출력메모리

def display():
    global window, canvas, paper, filename, inImageR, inImageG, inImageB, outImageR, outImageG,outImageB, inW, inH, outW, outH
    #기존에 캔버스 있으면 뜯어내기
    if canvas !=None:
        canvas.destroy()
    #화면준비 (고정됨)
    window.geometry(str(outH) + 'x' + str(outW))
    canvas = Canvas(window,width=outW, height=outH)
    paper = PhotoImage(width = outW,height=outH)
    canvas.create_image((outW/2,outH/2),image=paper,state='normal')
    #화면에 출력
    for i in range(outH):
        for k in range(outW):
            dataR = outImageR[i][k]
            dataG = outImageG[i][k]
            dataB = outImageB[i][k]
            paper.put('#%02x%02x%02x'% (dataR, dataG, dataB),(k,i))
    canvas.pack()
def equal():
    global window, canvas, paper, filename, inImageR, inImageG, inImageB, outImageR, outImageG,outImageB, inW, inH, outW, outH
    outW = inW
    outH = inH
    outImageR, outImageG, outImageB = [],[],[]
    tmpLIst = []
    for i in range(outH):  # 입력메모리 확보(0)으로 초기화
        tmpLIst = []
        for k in range(outW):
            tmpLIst.append(0)
        outImageR.append(tmpLIst[:])
        outImageG.append(tmpLIst[:])
        outImageB.append(tmpLIst[:])

    for i in range(inH):
        for k in range(inW):
            outImageR[i][k] = inImageR[i][k]
            outImageG[i][k] = inImageG[i][k]
            outImageB[i][k] = inImageB[i][k]
    display()


def saveFile():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    pass
def exitFile():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    pass

def addImage():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    outW = inW
    outH = inH
    outImage = []
    tmpLIst = []
    for i in range(outH):  # 입력메모리 확보(0)으로 초기화
        tmpLIst = []
        for k in range(outW):
            tmpLIst.append(0)
        outImage.append(tmpLIst)
    value = askinteger('밝게하기','밝게할 값-->',minvalue=1,maxvalue=255)
    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] +value >255:
                outImage[i][k]=255
            else:
                outImage[i][k] = inImage[i][k]+value
    display()

def subImage():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    outW = inW
    outH = inH
    outImage = []
    tmpLIst = []
    for i in range(outH):  # 입력메모리 확보(0)으로 초기화
        tmpLIst = []
        for k in range(outW):
            tmpLIst.append(0)
        outImage.append(tmpLIst)
    value = askinteger('어둡게하기','어둡게할 값-->',minvalue=1,maxvalue=255)
    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] - value < 0:
                outImage[i][k]= 0
            else:
                outImage[i][k] = inImage[i][k] - value
    display()
##전역 변수부
window, canvas, paper, filename = [None] *4
inImageR, inImageG, inImageB, outImageR, outImageG,outImageB = [],[],[],[],[],[]
inW, inH, outW, outH = [0]*4
## 메인 코드부
window = Tk()
window.geometry('400x400')
window.title('GIF 영상 처리 & 데이터 분석 Ver 0.01')
mainMenu = Menu(window);window.config(menu=mainMenu)
fileMenu = Menu(mainMenu);mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기', command=openFile)
fileMenu.add_command(label='저장', command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=exitFile)

pixelMenu = Menu(mainMenu)
mainMenu.add_cascade(label='화소점처리', menu=pixelMenu)
pixelMenu.add_command(label='동일영상', command=equal)



window.mainloop()



