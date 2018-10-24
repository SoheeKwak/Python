"""
     조건1. 5개 열중에서 Part Number와 Purchase Date는 제거한다.
     조건2. Supplier Y행은 지운다.
     조건3. 가격을 모두 1.5배 인상시킨다.
            그리고 100달러 미만 단위는 버린다. 770-->700
     이 결과를 result03, csv에 출력하시오.

     심화퀴즈: 열이 굉장히 많다고 가정해서 Part Number와 Purchase Date의 위치를 모른다.
     """

input_file = "D:\\workspace\\csv\\supplier_data.csv"
output_file = "D:\\workspace\\output\\result03.csv"

with open(input_file, 'r', newline='') as filereader :
    with open(output_file, 'w', newline='') as filewriter :

        header = filereader.readline()
        header  = header.strip() # 앞뒤 공백제거
        header_list = header.split(',')
        # Part Number, Purchase Date 찾기
        idx1 = 0
        for h in header_list :
            if h.strip().upper() == 'Part Number'.strip().upper() : # 모두 대문자로 변형해서 매칭(정확성을 위해)
                break
            idx1 += 1

        idx2 = 0
        for h in header_list :
            if h.strip().upper() == 'Purchase Date'.strip().upper() :
                break
            idx2 += 1
        if idx1 > idx2 :
            idx1, idx2 = idx2, idx1   # 밑에서  del(row_list[idx2])를 할때 뒤에것 idx2 부터 지워야 기존 위치 순서번호대로 지울 수 있음.

        # 리스트를 다시 콤마(,)로 분리된 문자열로 만들고 싶다.
        header_str = ','.join(map(str, header_list))
        filewriter.write(header_str + '\n')
        for  row  in  filereader :  # 모든행은 row에 넣고 돌리기.
            row = row.strip()
            row_list = row.split(',')
            del(row_list[idx2]) #뒤에서부터 지움
            del(row_list[idx1])
            if row_list[0] == 'Supplier Y' :
                continue
            cost = float(row_list[2][1:]) # 앞에 Part Number가 삭제됐으므로 2의 위치에 cost
            cost *= 1.5
            cost = int(cost/100) * 100  #100달러 미만 단위는 버린다. 770-->700
            cost_str = "${0:.2f}".format(cost)
            row_list[2] = cost_str
            row_str = ','.join(map(str, row_list))
            print(row_str)
            filewriter.write(row_str + '\n')