def read_car():
    f = open('car.csv', 'r')
    rows = []
    for row in f:
        # print(row)
        print(row.strip().split(','))# split: 콤마를 기준으로 ''(문자)로 변환시켜(문자가 하나라도 있으면 나머지도 문자화됨)리스트로 출력
mycar = read_car()