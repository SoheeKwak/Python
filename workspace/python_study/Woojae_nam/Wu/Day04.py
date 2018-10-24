"""
디지털 영상 처리(Digital Image Processing)
1)화소점 처리(Pixel Processing): 한개 점을 처리하기, 화소값이 변경
  ex)동일영상, 화소값반전, 밝게 하기(덧셈연산), 어둡게(뺄셈), 곱셈, 나눗셈,
     파라볼라(Cap,Cup), 감마
2)기하학 처리(Geometry Processing):한개 점을 처리. 화소값은 그대로, but 위치 변경
  ex)상하반전, 좌우반전, 이동, 회전, 확대, 축소
3)화소영역 처리(Area Processing):여러 개 점이 관련되어 처리
  ex)엠보싱, 블러링, 샤프닝, 에지검색(종류 수십개), 잡음제거
"""
## 영상 처리 및 데이터 분석 툴
from tkinter import *; import os.path ;import math
from  tkinter.filedialog import *
from  tkinter.simpledialog import *
## 함수 선언부
def loadImage(fname) :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    fsize = os.path.getsize(fname) # 파일 크기 확인
    inH = inW = int(math.sqrt(fsize))  # 입력메모리 크기 결정! (중요)
    inImage = []; tmpList = []
    for i in range(inH) :  # 입력메모리 확보(0으로 초기화)
        tmpList = []
        for k in range(inW) :
            tmpList.append(0)
        inImage.append(tmpList)
    # 파일 --> 메모리로 데이터 로딩
    fp = open(fname, 'rb') # 파일 열기(바이너리 모드)
    for  i  in range(inH) :
        for  k  in  range(inW) :
            inImage[i][k] =  int(ord(fp.read(1)))
    fp.close()

def openFile() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    filename = askopenfilename(parent=window,
                               filetypes=(("RAW파일", "*.raw"), ("모든파일", "*.*")))
    loadImage(filename) # 파일 --> 입력메모리
    equal() # 입력메모리--> 출력메모리
def saveFile():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    pass
def exitFile():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    pass

def display() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    # 기존에 캐버스 있으면 뜯어내기.
    if  canvas != None :
        canvas.destroy()
    # 화면 준비 (고정됨)
    window.geometry(str(outH) + 'x' + str(outW))
    canvas = Canvas(window, width=outW, height=outH)
    paper = PhotoImage(width=outW, height=outH)
    canvas.create_image((outW/2, outH/2), image=paper, state='normal')
    # 화면에 출력
    for i in range(outH) :
        for k in range(outW) :
            data = outImage[i][k]
            paper.put('#%02x%02x%02x' % (data, data, data), (k,i))
    canvas.pack()


def equal() :  # 동일 영상 알고리즘
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    # 중요! 출력메모리의 크기를 결정
    outW = inW;  outH = inH;
    outImage = [];   tmpList = []
    for i in range(outH):  # 출력메모리 확보(0으로 초기화)
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)
    #############################
    # 진짜 영상처리 알고리즘을 구현
    ############################
    for  i  in  range(inH) :
        for  k  in  range(inW) :
            outImage[i][k] = inImage[i][k]
    display()


def addImage() :  # 밝게하기 알고리즘
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    # 중요! 출력메모리의 크기를 결정
    outW = inW;  outH = inH;
    outImage = [];   tmpList = []
    for i in range(outH):  # 출력메모리 확보(0으로 초기화)
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)
    #############################
    # 진짜 영상처리 알고리즘을 구현
    ############################
    value = askinteger('밝게하기', '밝게할 값-->', minvalue=1, maxvalue=255)
    for  i  in  range(inH) :
        for  k  in  range(inW) :
            if inImage[i][k] + value > 255 :
                outImage[i][k] = 255
            else :
                outImage[i][k] = inImage[i][k] + value
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

def mulImage():
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
    value = askinteger('더욱밝게하기','더욱밝게할 값-->',minvalue=1,maxvalue=255)
    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] * value > 255:
                outImage[i][k]= 255
            elif inImage[i][k] * value < 0:
                outImage[i][k] = 0
            else:
                outImage[i][k] = inImage[i][k] * value
    display()

def divImage():
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
    value = askinteger('더욱어둡게하기','더욱어둡게할 값-->',minvalue=1,maxvalue=255)
    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] / value > 255:
                outImage[i][k]= 255
            elif inImage[i][k] / value < 0:
                outImage[i][k] = 0
            else:
                outImage[i][k] = inImage[i][k] / value
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
pixelMenu.add_command(label='밝게하기', command=addImage)
pixelMenu.add_command(label='더욱밝게하기', command=mulImage)
pixelMenu.add_command(label='어둡게하기', command=subImage)
pixelMenu.add_command(label='더욱어둡게하기', command=divImage)



window.mainloop()

