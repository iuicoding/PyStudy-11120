score = float(input("> 만족도를 입력해주세요: "))
# if - elif
if score == 5:
    print("완벽")
elif 4.5 <= score:
    print("매우 만족")
# if not
if not (score == 5):
    print("5가 아니네")
# if a and b
if score == 5 and score - 1 == 4:
    print("점수는 5가 맞네")
# if - else
if 2 <= 3:
    print("2 <= 3")
else:
    print("아니네")

# 리스트 선언하고 출력
alist = [1, 2, 3, 4, 5]

print(alist)

#비교 연산자 사용하기
if 4 in alist:
    print("4가 있네")

if 121 not in alist:
    print("121없음 뭐임")

#특정 위치에 있는 요소 출력하기
print(alist[1])



#리스트에 집어넣기
alist = alist + [1]
alist = alist * 2
alist.append(8)
print(alist)
#리스트에서 제거하기
del alist[0]
alist.remove(2)
alist.pop(4)
alist.pop()
print(alist)
#비파괴적으로 요소 제거 (연산 적용 X)
print(alist + [2])
print(alist * 3)
#for 반복문 적용하기
for element in a:
    print(element)
