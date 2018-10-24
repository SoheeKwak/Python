
# emails = ['python@mail.example.com', 'python+kr@example.com',              # 올바른 형식
#           'python-dojang@example.co.kr', 'python_10@example.info',         # 올바른 형식
#           'python.dojang@e-xample.com',                                    # 올바른 형식
#           '@example.com', 'python@example', 'python@example-com']          # 잘못된 형식
#
# 아래와 같은 결과가 출력되는 정규식을 만드세요.
# True True True True True False False False
import re

emailPat = re.compile("python([^0-9A-Za-z]|[a-z]|[0-9])*@[a-z|\.]*e[-]*xample\.[a-z]")
res = emailPat.match(input("메일 주소를 입력하세요:"))
if res == None :
    print("False")
else :
    print("True")

import re
p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
"""
아이디@도메인.최상위도메인
"""
