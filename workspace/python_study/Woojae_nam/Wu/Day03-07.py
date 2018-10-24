##텍스트 파일 처리 1 (열기-->작업하기-->닫기)

fname = 'c:/windows/win.ini' #원래 있는 파일
fname2 = 'my.txt' #복사될 파일

with open(fname,'r') as rfp:       #첫 번째 코드 방법
    with open(fname2,'w') as wfp:
        inList = rfp.readlines()
        for inStr in inList:
            wfp.writelines(inStr)


# with open(fname,'r') as rfp:       #두 번째 코드 방법
#     with open(fname2,'w') as wfp:
#         while True:
#             inStr = rfp.readline()
#             if inStr == '' or inStr == None:  # if not inStr
#                 break
#             wfp.writelines(inStr)



# rfp = open(fname,'r')         #세 번째 코드 방법
# wfp = open(fname2,'w')
# while True:
#     inStr = rfp.readline()
#     if inStr=='' or inStr==None: # if not inStr
#         break
#     wfp.writelines(inStr)
#     print(inStr, end='')
# rfp.close()
# wfp.close()
print('Ok')