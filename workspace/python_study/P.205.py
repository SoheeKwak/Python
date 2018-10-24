animals = {'닭':'병아리', '개':'강아지','곰':'능소니','고등어':'고도리','명태':'노가리','말':'망아지',
        "호랑이":"개호주"};
while (True) :
    mypet = input(str(list(animals.keys())) + " 중 새끼 이름을 알고 싶은 동물은?")
    if mypet in animals :
       print("<%s> 새끼는<%s>입니다." % (mypet, animals.get(mypet)))
    elif mypet == "끝" :
       break
    else :
       print("그런 동물이 없음. 확인 요망.")