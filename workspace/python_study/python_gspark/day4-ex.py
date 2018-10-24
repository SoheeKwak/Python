import re
f = open("words.txt", "r")
lines = f.readlines()
f.close()
count = 0
for line in lines:
    if len(line) <= 11 :
        count += 1

print(count)


wordNum = int(input("단어 갯수를 입력하세요:"))
text = input("문자를 입력하세요:")
textList = text.split()
if (len(textList)) < wordNum :
    print("wrong")


grams = [textList[i:i+wordNum] for i in range(len(textList)-(wordNum-1))]
for gram in grams :
     print(gram)
#또는
nGram= list(zip(*[textList[i:] for i in range(7)]))
print(nGram)


