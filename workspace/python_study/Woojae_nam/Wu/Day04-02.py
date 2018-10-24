##영상 처리 및 데이터 분석 툴
from tkinter import *
from tkinter.filedialog import *
import os.path
import math
from tkinter.simpledialog import *

##함수 선언부
def loadImage(fname):
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    fsize = os.path.getsize(fname) #파일 크기 확인
    inH = inW = int(math.sqrt(fsize)) #중요!! 입력 메모리 크기 결정
    inImage = []
    tmpLIst = []
    for i in range(inH): #입력메모리 확보(0)으로 초기화
        tmpLIst =[]
        for k in range(inW):
            tmpLIst.append(0)
        inImage.append(tmpLIst)
    #파일--> 메모리로 데이터 로딩
    fp = open(fname, 'rb') #파일열기 (바이너리)
    for i in range(inH):
        for k in range(inW):
            inImage[i][k] = int(ord(fp.read(1)))
    fp.close()
    # print(inImage[100][100])
def openFile():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    filename = askopenfilename(parent=window,
                               filetypes=(("RAW파일", "*.raw"), ("모든파일", "*.*")))
    loadImage(filename) #파일 -->입력메모리
    equal() #입력 메모리-->출력메모리

def display():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
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
            data = outImage[i][k]
            paper.put('#%02x%02x%02x'% (data, data, data),(k,i))
    canvas.pack()
def equal():
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

    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = inImage[i][k]
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
inImage, outImage = [],[]
inW, inH, outW, outH = [0]*4
## 메인 코드부
window = Tk()
window.geometry('400x400')
window.title('영상 처리 & 데이터 분석 Ver 0.05')
mainMenu = Menu(window);window.config(menu=mainMenu)
fileMenu = Menu(mainMenu);mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기', command=openFile)
fileMenu.add_command(label='저장', command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=exitFile)

pixelMenu = Menu(mainMenu)
mainMenu.add_cascade(label='화소점처리', menu=pixelMenu)
pixelMenu.add_command(label='동일영상', command=equal)
pixelMenu.add_command(label='밝게하기', command=addImage())
pixelMenu.add_command(label='어둡게하기', command=subImage())


window.mainloop()



