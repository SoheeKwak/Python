import re

emails = ['python@mail.example.com', 'python+kr@example.com',              # 올바른 형식
          'python-dojang@example.co.kr', 'python_10@example.info',         # 올바른 형식
          'python.dojang@e-xample.com',                                    # 올바른 형식
          '@example.com', 'python@example', 'python@example-com']          # 잘못된 형식

pat = re.compile("(\w+[\w\.]*)@(\w+[\w\.-]*)\.([A-Za-z]+)")

for i in range (0,len(emails)) :
    res = pat.search(emails[i])
    if res == None :
        print("False")
    else:
        print("True")
