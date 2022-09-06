while True:
    x = int(input("거리를 입력하세요"))
    if x < 30:
        print(2000)
    elif x < 60:
        print(3000)
    elif x < 100:
        print(3500)
    elif x < 150:
        print(4000)
    else:
        print(4500)