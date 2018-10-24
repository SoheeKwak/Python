input_file = "D:\\workspace\\csv\\supplier_data.csv"
output_file = "D:\\workspace\\output\\result02.csv"

with open(input_file,'r', newline='') as filereader:
    with open(output_file,'w', newline='') as filewriter:


    ## 각 금액(값, Cost)을 모두 100$ 인상시킨 것을 result02,csv에 출력하시오.

        header = filereader.readline()
        header = header.strip() #앞뒤 공백제거
        header_list = header.split(',')
        # 리스트를 다시 콤마(,)로 분리된 문자열로 만들고 싶다.
        header_str = ','.join(map(str, header_list))
        filewriter.write(header_str + '\n')

        for row in filereader : #모든 행을 row에 넣고 돌리기
            row = row.strip()
            row_list = row.split(',')
            cost = float(row_list[3][1:]) # [1:] 리스트의 각요소가 string이기 때문에 $(0의 요소)를 제외한 뒤 숫자만 추출
            cost +=100
            cost_str = "${0:.2f}".format(cost)
            row_list[3] = cost_str
            row_str = ','.join(map(str,row_list))
            print(row_str)
            filewriter.write(row_str + '\n')

        """
        조건1. 5개 열중에서 Part Number와 Purchase Date는 제거한다.
        조건2. Suplier Y행은 지운다.
        조건3. 가격을 모두 1.5배 인상시킨다.
            그리고 100달러 미만 단위는 버린다. 770-->700
        이 결과를 result02, csv에 출력하시오.
        """