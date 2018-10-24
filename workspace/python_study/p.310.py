from tkinter import*

window = Tk()

mainMenu = Menu(window)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)

saveMenu = Menu(fileMenu)
fileMenu.add_cascade(label = "저장", menu = saveMenu)
saveMenu.add_command(label="다른이름으로 저장")
fileMenu.add_command(label="열기")

fileMenu.add_separator()
fileMenu.add_command(label="페이지설정")
printMenu = Menu(fileMenu)
fileMenu.add_cascade(label="인쇄", menu=printMenu)
printMenu.add_command(label="미리보기")
printMenu.add_command(label="프린트")


fileMenu.add_separator()
fileMenu.add_command(label="종료")


editMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "편집", menu = editMenu)
editMenu.add_cascade(label = "붙여넣기")

editMenu.add_separator()
editMenu.add_command(label="바꾸기")
editMenu.add_command(label="이동")

fontMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "서식", menu = fontMenu)
fontMenu.add_cascade(label = "자동줄바꿈")
fontMenu.add_cascade(label = "글꼴")

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "보기", menu = fileMenu)
fileMenu.add_cascade(label = "상태표시줄")

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "도움말", menu = fileMenu)
fileMenu.add_cascade(label = "도움말보기")
fileMenu.add_separator()
fileMenu.add_command(label="메모장정보")

window.mainloop()
