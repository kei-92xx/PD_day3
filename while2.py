#정수를 입력받는다 음수가 입력될때까지 양의정수나 0을 입력받아 합계와 평균을 구하자

#1. 입력변수를 지정한다
nums = [] #값들을 저장할 변수를 지정한다 []또는 list

num = int(input("정수 : "))
while num>=0:
    nums.append( num )
    num = int(input("정수 : "))

print( nums )
sum=0
for i in range(0, len(nums)):
    sum = sum + nums[i]

print(f"합계 : {sum} 평균:{sum/len(nums)}")

#문제1 : 정수를 음수가 입력될때까지 입력을 받아서
#       각각 짝수와 홀수를 구분해서 짝수와 합계와 홀수의 합계를 출력한다




#문제2 : 정수를 음수가 입력될때까지 입력을 받아서
#       각각 짝수와 홀수를 구분해서 분리시켜서 다른 리스트에 담아서 한번에 출력