# ord("문자") -> 해당문자에 대한 unicode를 반환한다
print( ord("A") ) #65
print( ord("B") ) #66
print( ord("C") ) #67
print( ord("a") ) #97
print( ord("b") ) #98
print( ord("0") ) #48
print( ord("1") ) #49
print( ord("2") ) #50

#ord의 반대역할 - chr(숫자) => 문자
print( chr(65))
print( chr(66))
print( chr(67))

#알파벳을 for문 사용해서 대문자로 출력하기

for i in range(0, 26):
    print( chr(i+65), end=' ')
print()

#알파벳을 for문 사용해서 대문자로 출력한 뒤 맨 앞의 알파벳이 뒤로 가게 출력 원래의 알파벳 순서로 돌아오기 전 까지

for i in range(0, 26):
    k=i
    for j in range(0, 26):
        print( chr(k+65), end=' ')
        k=k+1
        if k>25:
            k=0
    print()
