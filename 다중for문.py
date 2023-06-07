#for문 안에 또 for문이 있다
"""
for i in range(1, 6):           i=1 j=1,2,3,4,5
    for j in range(1, 6):       i=2 j=1,2,3,4,5
        코드                    i=3 j=1,2,3,4,5
                                i=4 j=1,2,3,4,5
                                i=5 j=1,2,3,4,5
"""

for i in range(1,6):
    print("i=", i, " j=", end='')
    for j in range(1,6):
        print(j, end = ' ') #옆으로 출력하기
    print() #줄바꿈

#이중 for문을 사용해서 도형을 만들 수 있다
for i in range(1, 6):
    for j in range(1, 6):
        print("*", end='')
    print()
    
#삼각형
for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end='')
    print()
    
"""
#다이아몬드        라인수   공백개수  별개수
    *                1       3        1
   ***               2       2        3
  *****              3       1        5
 *******             4       0        7

  *****              1       1        5   
   ***               2       2        3
    *                3       3        1

라인수 공백개수        i  공백수 : LINE-i+1
  1      3      4
  2      2      4
  3      1      4
  4      0      4
"""
#다이아몬드
LINE = 5
for i in range(0, LINE):
    #공백출력
    for j in range(0, LINE-i):
        print(' ', end='')
    #별그리기
    for j in range(0, 2*i-1):
        print('*', end='')
    print()   

#다이아몬드 역으로
for i in range(0, LINE):
    for j in range(0, i):
        print(' ', end='')
    for j in range(0, (LINE-i)*2-1):
        print('*', end='')
    print()