#문제1 : 정수를 음수가 입력될때까지 입력을 받아서 각각 짝수와 홀수를 구분해서 짝수와 합계와 홀수의 합계를 출력한다

nums = [] #값들을 저장할 변수를 지정한다 []또는 list

num = int(input("정수 : "))
while num>=0:
    nums.append( num )
    num = int(input("정수 : "))

print( nums )

even_sum = 0 #짝수 합계를 구할 변수
even_cnt = 0 #짝수 개수를 셀 변수

odd_sum = 0 #홀수 합계를 구할 변수
odd_cnt = 0 #홀수 개수를 셀 변수

for n in nums: #nums 라는 리스트로부터 데이터를 하나씩 n에 전달한다
    if n%2==0:
        even_sum = even_sum + n
        even_cnt = even_cnt + 1
    else:
        odd_sum = odd_sum + n
        odd_cnt = odd_cnt + 1
print(even_sum, even_cnt)
print(odd_sum, odd_cnt)