# 5. 정제된 파일을 읽어서 형태소 분석->명사추출->빈도수
# 6. 명사로 구성된 단어별 빈도수를 텍스트 파일로 저장(output_final.txt)

from konlpy.tag import Twitter
from collections import Counter # Counter:클래스  collections:모듈

# colors = ['r', 'b', 'r', 'g', 'b', 'b']
# num = [1,2,3,3,3,4,4,4,4,4,5]
# cnt = Counter(colors)
# print(cnt) # Counter({'b': 3, 'r': 2, 'g': 1})
# # Counter는 리스트 또는 튜플에 저장된 데이터를 딕셔너리 형태로 데이터가 등장한 횟수를 출력
# n = Counter(num)
# print(n.most_common()) # [(4, 5), (3, 3), (1, 1), (2, 1), (5, 1)] 빈도순으로 출력
# print(n.most_common(3)) #[(4, 5), (3, 3), (1, 1)] 상위 최대 빈도 3개 출력

def get_tags(gtext, ntags=30): #명사를 추출하는 함수, ntags=30는 default로 설정하여 밑에서 noun_count를 안써도 30으로 자동 설정된
    twitter=Twitter()
    nouns = twitter.nouns(gtext)
    # print(nouns)
    count = Counter(nouns)
    # print(count)
    # print(count.most_common(ntags)) #튜플로 나옴 [('날씨', 5), ('비', 5), ('오늘', 5),...('발효', 2)]
    return_list = []
    for word, cnt in count.most_common(ntags):
        temp = {'tag':word, 'count':cnt} #tag:키 count:값
        # print(temp)
        return_list.append(temp)
    return return_list

def main():
    text_file_name = "output_cleaned.txt"
    noun_count = 30
    output_file_name = "output_final.txt"
    open_text_file = open(text_file_name, "r")
    text = open_text_file.read()
    res = get_tags(text, noun_count)
    open_text_file.close()

    open_output_file = open(output_file_name, "w")
    for data in res:
        noun = data['tag']
        count = data['count']
        open_output_file.write("{} {}\n".format(noun, count)) #{} {}\n 이 문자열에 대해서 noun, count의 format으로 출력하라.

if __name__ =='__main__':
    main()

