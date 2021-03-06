## 영상 처리 및 데이터 분석 툴
from tkinter import *; import os.path ;import math
from  tkinter.filedialog import *
from  tkinter.simpledialog import *
import operator
## 함수 선언부
def loadImage(fname) :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    fsize = os.path.getsize(fname) # 파일 크기 확인
    inH = inW = int(math.sqrt(fsize))  # 입력메모리 크기 결정! (중요), 정방형 파일 선택
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
            inImage[i][k] = int(ord(fp.read(1)))
    fp.close()

def openFile() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    filename = askopenfilename(parent=window,
                               filetypes=(("RAW파일", "*.raw"), ("모든파일", "*.*")))
    loadImage(filename) # 파일 --> 입력메모리
    equal() # 입력메모리--> 출력메모리

import struct
def saveFile():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    saveFp = asksaveasfile(parent=window, mode='wb',
                           defaultextension="*.raw", filetypes=(("RAW파일", "*.raw"), ("모든파일", "*.*")))
    for i in range(outW):
        for k in range(outH):
            saveFp.write(struct.pack('B', outImage[i][k]))

    saveFp.close()

def exitFile():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    window.quit()
    window.destroy

import threading
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
    def putPixel() :
        for i in range(0, outH) :
            for k in range(0, outW) :
                data = outImage[i][k]
                paper.put('#%02x%02x%02x' % (data, data, data), (k,i))

    threading.Thread(target=putPixel).start()
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

def reverse() :  # 화소값반전 영상 알고리즘
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
            outImage[i][k] = 255 - inImage[i][k]

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
    value = askinteger('선명하게하기','선명하게할 값-->',minvalue=1,maxvalue=255)
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
    value = askinteger('탁하게하기','탁하게할 값-->',minvalue=1,maxvalue=255)
    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] / value > 255:
                outImage[i][k]= 255
            elif inImage[i][k] / value < 0:
                outImage[i][k] = 0
            else:
                outImage[i][k] = inImage[i][k] / value
    display()

def paraCap() :  # 파라볼라 캡.
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH

    Lookup = [0] * 256
    for i in range(256) :
        Lookup[i] = int(255 - 255.0 * (( i / 128.0 - 1) * ( i / 128.0 - 1)))

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
                outImage[i][k] = Lookup[inImage[i][k]]
    display()

def upDown() :  # 상하 반전 알고리즘
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
            outImage[outW-1-i][k] = inImage[i][k]
    display()

def mirrorImage(): #좌우 반전 알고리즘
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
            outImage[i][outH-1-k] = inImage[i][k]
    display()

def average(): #입출력 영상의 평균값
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    rawSum = 0
    for i in range(inH):
        for k in range(inW):
            rawSum += inImage[i][k]
    inRawAvg = int(rawSum / (inH*inW))

    rawSum = 0
    for i in range(outH):
        for k in range(outW):
            rawSum += outImage[i][k]
    outRawAvg = int(rawSum / (outH * outW))

    cutRawSum = 0
    rate = 0
    rate = askinteger('상하위구간 제거하기','제거할 값(%)-->',minvalue=1,maxvalue=100)
    for i in range(inH):
        if i >=inH *(rate/100) and i <=inH *(100-rate)/100:
            for k in range(inW):
               if k >=inW *(rate/100) and k <= inW *(100-rate)/100:
                   cutRawSum += inImage[i][k]
    inH = inH - (inH * (rate*2/ 100))
    inW = inW - (inW * (rate*2/ 100))
    cut_inRawAvg = int(cutRawSum / (inH * inW))

    for i in range(outH):
        if i >= outH * (rate/100) and i <= outH * (100-rate)/100:
            for k in range(outW):
                if k >= outW * (rate/100) and k <= outW * (100-rate)/100:
                    cutRawSum += outImage[i][k]
    outH = outH - (outH * (rate*2/ 100))
    outW = outW - (outW * (rate*2/ 100))
    cut_outRawAvg = int(cutRawSum / (outH * outW))

    subWindow = Toplevel(window) #부모(window)에 종속된 서브윈도
    subWindow.geometry('400x100')
    label1 = Label(subWindow, text='입력영상 평균값, 출력영상 평균값 -->' + str(inRawAvg)+ str(outRawAvg))
    label1.pack()
    label2 = Label(subWindow, text='입력영상 구간 평균값, 출력영상 구간 평균값 -->'+ str(cut_inRawAvg) + str(cut_outRawAvg))
    label2.pack()
    subWindow.mainloop()

def max_min():
    global inImage, outImage, inH, inW, outH, outW
    inDic, outDic = {},{}  # 색상: 개수 딕셔너리
    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] in inDic:
                inDic[inImage[i][k]] += 1
            else:
                inDic[inImage[i][k]] = 1
    for i in range(outH):
        for k in range(outW):
            if outImage[i][k] in outDic:
                outDic[ outImage[i][k]] += 1
            else:
                outDic[ outImage[i][k]] = 1
    incountList = sorted(inDic.items(), key=operator.itemgetter(1))
    outcountList = sorted(outDic.items(), key=operator.itemgetter(1))
    subWindow = Toplevel(window)  # 부모(window)에 종속된 서브윈도
    subWindow.geometry('200x100')
    label1 = Label(subWindow, text='입력영상 빈도수 최소값, 최대값 -->' +str(incountList[0])+str(incountList[-1]))
    label1.pack()
    label2 = Label(subWindow, text='출력영상 빈도수 최대값, 최소값 -->' +str(outcountList[0])+str(outcountList[-1]))
    label2.pack()
    subWindow.mainloop()


def panImage():
    global panYN
    panYN = True
def mouseClick(event) :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, sx,sy,ex,ey, panYN
    if not panYN:
        return
    sx = event.x  #마우스 start
    sy = event.y
def mouseDrop(event):
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, sx,sy,ex,ey, panYN
    if not panYN:
        return
    ex = event.x  #마우스 end
    ey = event.y
    mx = sx - ex #마우스 move(start->end)
    my = sy - ey
    # 중요! 출력메모리의 크기를 결정
    outW = inW;  outH = inH
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
            if 0 <= i-my < outH and k-mx < outW:
                outImage[i-my][k-mx] = inImage[i][k]
    panYN = False
    display()

def zoomOut() :  # 축소하기 알고리즘
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    # 중요! 출력메모리의 크기를 결정
    scale = askinteger('축소하기', '축소할 값-->', minvalue=2, maxvalue=32)
    outW = int(inW/scale);  outH = int(inH/scale)
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
            outImage[int(i/scale)][int(k/scale)] = inImage[i][k]
    display()

def zoomIn() :  # 확대하기 알고리즘
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    # 중요! 출력메모리의 크기를 결정
    scale = askinteger('확대하기', '확대할 값-->', minvalue=2, maxvalue=32)
    outW = int(inW * scale);  outH = int(inH * scale)
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
            outImage[int(i * scale)][int(k * scale)] = inImage[i][k]
    display()

def zoomIn_clear():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    # 중요! 출력메모리의 크기를 결정
    scale = askinteger('선명하게 확대하기', '선명하게 확대할 값-->', minvalue=2, maxvalue=32)
    outW = int(inW * scale);
    outH = int(inH * scale)
    outImage = [];
    tmpList = []
    for i in range(outH):  # 출력메모리 확보(0으로 초기화)
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)
    #############################
    # 진짜 영상처리 알고리즘을 구현
    ############################
    for i in range(outH):
        for k in range(outW):
            outImage[i][k] = inImage[int(i/scale)][int(k/scale)]
    display()


##전역 변수부
window, canvas, paper, filename = [None] *4
inImage, outImage = [],[]
inW, inH, outW, outH = [0]*4
panYN = False
sx,sy,ex,ey = [0]*4

## 메인 코드부
window = Tk()
window.title('영상 처리 & 데이터 분석 Ver 0.2')
window.bind("<Button-1>", mouseClick)
window.bind("<ButtonRelease-1>", mouseDrop)

mainMenu = Menu(window);window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기', command=openFile)
fileMenu.add_command(label='저장', command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=exitFile)

pixelMenu = Menu(mainMenu)
mainMenu.add_cascade(label='화소점처리', menu=pixelMenu)
pixelMenu.add_command(label='동일영상', command=equal)
pixelMenu.add_command(label='화소값반전', command=reverse)
pixelMenu.add_command(label='밝게하기', command=addImage)
pixelMenu.add_command(label='어둡게하기', command=subImage)
pixelMenu.add_command(label='선명하게하기', command=mulImage)
pixelMenu.add_command(label='탁하게하기', command=divImage)
pixelMenu.add_command(label='파라볼라', command=paraCap)



analyzeMenu = Menu(mainMenu)
mainMenu.add_cascade(label='데이터분석', menu=analyzeMenu)
analyzeMenu.add_command(label='평균값/상하위제거 구간평균값', command=average)
analyzeMenu.add_command(label='빈도수 최대/최소값', command=max_min)

geoMenu = Menu(mainMenu)
mainMenu.add_cascade(label='기하학 처리', menu=geoMenu)
geoMenu.add_command(label='상하반전', command=upDown)
geoMenu.add_command(label='좌우반전', command=mirrorImage)
geoMenu.add_command(label='화면이동', command=panImage)
geoMenu.add_command(label='화면축소', command=zoomOut)
geoMenu.add_command(label='화면확대', command=zoomIn)
geoMenu.add_command(label='선명한화면확대', command=zoomIn_clear)




window.mainloop()

