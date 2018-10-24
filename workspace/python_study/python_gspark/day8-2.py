# 3. 데이터 정제(크리닝)-영어, 특수기호 제거(정규식)
# 4. 정제된 경과를 텍스트 파일로 저장(output_cleaned.txt)
import re

INPUT_FILE_NAME = "output.txt"
OUTPUT_FILE_NAME = "output_cleaned.txt"

# 정제 함수
def clean_text(myText):
    cleaned_text = re.sub('[a-zA-Z]', '', myText)
    cleaned_text = re.sub('[\{\}\[\]\(\)\\\/▶_↑…㎜.,:;\'\"]', '', cleaned_text) #{}[]-#()\''"" 등 툭수문자를 소거할 떄는 \기호를 제거하는 특수문자 앞에 붙여줌
    return cleaned_text

# 메인 함수
def main():
    read_file = open(INPUT_FILE_NAME, "r")
    write_file = open(OUTPUT_FILE_NAME, "w")
    text = read_file.read()
    print("before:")
    print(text)
    cleaned_text = clean_text(text) #위 def clean_text(text)를 호출하기 위해 입력파일(output.txt)을 먼저 읽음. 읽은 파일을 위def로 보내서 정제한 후 다시 갖고 와서 출력함
    print("after:")
    print(cleaned_text)
    write_file.write(cleaned_text)
    read_file.close()
    write_file.close()

if __name__ == "__main__":
    main()
