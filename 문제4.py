#문제1. 다음 반복문 내부에 if 조건문의 조건식을 채워서 100 이상의 숫자만 출력하게 만들어 보세요
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for numbers in numbers:
    if numbers >= 100:
        print("- 100 이상의 수:", numbers)


#문제2. 다음 빈칸을 채워서 실행 결과에 해당하는 프로그램들을 완성해보세요
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for num in numbers:
    if num%2==0:
        print(f"{num}은 짝수입니다")
    else:
        print(f"{num}은 홀수입니다")
        
for num in numbers:
    if num//100>0:
        print(f"{num}은 백의자리수 입니다")
    elif num//10>0:
        print(f"{num}은 십의자리수 입니다")
    else:
        print(f"{num}은 일의자리수 입니다")
        
#문제. 동전 거스르기
#거스름돈 : 78767
#  50000 - 1장, 10000 - 2장, 5000 - 1장, 1000 - 3장, 500 - 1개, 100 - 2개, 50 - 1개, 10 - 1개

money_u = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
money_c = [ 0, 0, 0, 0, 0, 0, 0, 0]

coins = 78767
temp = coins

""" (노가다 영역)
money_c[0] = temp // money_u[0]
temp = temp % money_u[0]

money_c[1] = temp // money_u[1]
temp = temp % money_u[1]
print( money_c )
"""

for i in range(0, len(money_u)):
    money_c[i] = temp // money_u[i]
    temp = temp % money_u[i]
    
print( money_c)


