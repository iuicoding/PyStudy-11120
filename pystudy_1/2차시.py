score = float(input("> 만족도를 입력해주세요: "))
if score == 5:
    print("완벽")
elif 4.5 <= score:
    print("매우 만족")
elif 3.5 <= score:
    print("만족")
elif 2.5 <= score:
    print("보통")
elif 1.5 <= score:
    print("불만족")
elif 0.5 <= score:
    print("매우 불만족")
else:
    print("이런게 다 있네")

