# 1.텍스트 분류
# - 스팸/햄 메일 분류, 카테고리 분류
# - 가장 많이 사용되는 방법:베이즈 정리를 이용한 텍스트 분류방법인 '베이지안 필터'
# 
# 2.머신러닝
# - 교사, 비교사, 강화학습
# - 베이지안 필터는 교사 학습에 해당
# 
# 3. 모델 생성 과정
# 스팸/햄 메일 입력 -> 메일내용 학습 -> 모델
# 새로운 메일 입력 -------------------> 스팸/햄 분류 결과 출력
# 
# 4. 모델 성능 평가
# - precision, recall, f-measure, support
# 
# 5. false positive/false negative
#    true positive/true negative
# 
# 6. 조건부 확률
# - 어떤 A라는 사건이 일어났다는 조건 하에서 다른 사건 B가 일어날 확률
# - P(B|A)
# - 비가 내릴 확률 :P(비), 교통사고가 발생할 확률:P(교통사고)
# - 비가 내리는 날에 교통사고가 발생할 확률? P(교통사고|비)

# 딕셔너리 중첩 참고
test = {'gildong':{'w':70, 'h':170, 'b':'a'},
        'donggil': {'w': 75, 'h': 160, 'b': 'ab'},
        'gildo': {'w': 72, 'h': 150, 'b': 'o'}}
print(test)
print(test['gildong'])
test['gildong']['h']+=10
print(test)
test['gildong']['h']=200
print(test)

for n in test:
    print(n)