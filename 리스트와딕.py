"""
홍길동, 90, 80, 70
장길산, 100, 100, 90
임꺽정, 80, 70, 60
list안에 dict으로 넣어놓고 총점, 평균 구해서 출력하기
"""

scoreList = [
    {"name":"홍길동","kor":90, "eng":80, "mat":70},
    {"name":"장길산","kor":100, "eng":100, "mat":90},
    {"name":"임꺽정","kor":80, "eng":70, "mat":60},
]

for score in scoreList:
    score['total'] = score['kor'] + score['eng'] + score['mat']
    score['avg']= score['total']/3

for s in scoreList:
    print(f"{s['name']} {s['kor']} {s['eng']} {s['mat']} {s['total']} {s['avg']}")
    