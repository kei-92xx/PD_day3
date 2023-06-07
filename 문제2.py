#문제2 : 리스트 내 짝수와 홀수를 구분해서 분리시켜서 다른 리스트에 담아서 한번에 출력

nums = [1,2,3,4,5,6,7,8,9,10,11,12] #값들을 저장할 변수를 지정한다 []또는 list
#짝수를 저장할 list
even_list = []
#홀수를 저장할 list
odd_list = []

for n in nums:
    if n%2==0:
        even_list.append(n)
    else:
        odd_list.append(n)

print( even_list )
print( odd_list )
