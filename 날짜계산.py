#연도 월 일을 입력받아서 그날이 그해의 몇번째 날인지 맞추기
#윤년 - 4의 배수가 되면서 100의 배수가 되면 안되고 400의 배수는 윤년이다
#윤년의 경우 2월이 29일 된다. 유년 아니면 28일이 된다.
year = int(input("연도 "))

#and, or, not : 논리연산자 결과는 True 또는 False 이다
# 조건식1 and 조건식2 : 두개의 조건식이 둘다 True일때 True 아니면 False이다
# 조건식1 or 조건식2 : 두개의 조건식중 하나라도 True이면 True 아니면 False이다
# not 조건식 : True -> False 로 False -> True
# 우선순위 : not -> and -> or 순으로 적용된다.
if year%4==0 and year%100!=0 or year%400==0:
    print("윤년임")
else:
    print("윤년아님")

year = int(input("연도 : "))
month = int(input("월 : "))
day = int(input("일 : "))
 
moth_last =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year%4==0 and year%100!=0 or year%400==0:
    moth_last[1] = 29

days = 0
for i in range(0, month-1):
    days = days + moth_last[i]
    
days = days + day
print(f"{days}번째 날입니다")