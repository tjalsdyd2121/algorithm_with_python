index = 'test'
print(index[-2]) # 뒤에서 2번째 문자 출력

print(index[0:5]) # 0부터 4번째 인덱스 슬라이싱
print(index[:5]) # 0부터 4번째 인덱스 슬라이싱
print(index[:]) # 전체 문자열 출력
print(index[0:-3]) # 0부터 (4-3)-1 == 0번째 인덱스 슬라이싱
print(index[0:]) # 0부터 -1번째 인덱스 슬라이싱 -> 공백