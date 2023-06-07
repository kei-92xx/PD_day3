#문제:
# 1 2 3 4 5 6 7 8 9 10
# 11 12 13 14 15 16 17 18 19 20
# 1~100까지 한줄에 열개씩, 이중 for문 사용하기

k=1
for i in range(1,11):
    for j in range(1,11):
        print(k, end=' ')
        k = k + 1
    print() #줄바꿈
