# 1. 오늘의 날씨 스크랩(네이버)
# 2. 날씨 본문 내용을 텍스트 파일로 저장(output.txt)
# 3. 데이터 정제(크리닝)-영어, 특수기호 제거(정규식)
# 4. 정제된 결과를 텍스트 파일로 저장(output_cleaned.txt)
# 5. 정제된 파일을 읽어서 형태소 분석->명사추출->빈도수
# 6. 명사로 구성된 단어별 빈도수를 텍스트 파일로 저장(output_final.txt)
# 7. 상위 10개에 해당하는 단어를 시각화
#
# 8. 협업 필터링(기계학습, 추천시스템)
# 9. 긍정/부정 감성분석 (Word2Vec, RNN(LSTM))
# 10. 마르코프 기반 문장 이해/생성(정확도는 딥러닝보다 다소 떨어짐, 기계학습)


# 1. 오늘의 날씨 스크랩(네이버)
# 2. 날씨 본문 내용을 텍스트 파일로 저장(output.txt)

from bs4 import BeautifulSoup
import urllib.request as req

OUTPUT_FILE_NAME = 'output.txt'
URL = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=103&oid=422&aid=0000333483"

#크롤링 함수
def get_text(URL):
    sourceFromURL = req.urlopen(URL)
    soup = BeautifulSoup(sourceFromURL, 'lxml', from_encoding='utf-8') #lxml 대신 html parser로 대체해도 무방
    text=""
    for item in soup.find_all('div', id='articleBodyContents'): #이 기사 같은 경우는 div=id "articleBodyContents"가 하나밖에 없으므로 soup.find로 써도 무방(for도 생략 가능)
        text = text+str(item.find_all(text=True)) # text=True :태그들은 제거된 텍스트 추출
    print(text)
    return text


def main():
    open_output_file = open(OUTPUT_FILE_NAME, "w")
    res = get_text(URL)
    open_output_file.write(res)
    open_output_file.close()

if __name__ == '__main__': #(다른 파일에서 이 모듈을 import할 때 이 파일의 print결과까지 가져오지 않고 함수만 가져오고자 할 때 main함수를 씀)
    main() #메인함수를 호출해라. 바로 위 def main():으로 가서 호출
