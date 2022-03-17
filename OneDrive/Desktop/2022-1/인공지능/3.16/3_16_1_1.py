print("001 print 기초")
print("Hello World")
print(" ")

print("002 print 기초")
print("Mary\'s cosmetics")
print(" ")

print("003 print 기초")
print('신씨가 소리질렀다. "도둑이야".')
print(" ")

print("004 print 기초")
print('"C:\Windows"')
print(" ")

print("005 print 기초")
print('안녕하세요.\n만나서\t\t반갑습니다.')
print("'\\n'은 줄바꿈, \\t는 tab의 역할을 한다.")
print(" ")

print("051 리스트 생성")
movie_rank = ['닥터 스트레인지','스플릿','럭키']
print(movie_rank)
print(" ")

print("052 리스트에 원소 추가")
movie_rank.append("배트맨")
print(movie_rank)
print(" ")

print("053")
movie_rank.insert(1,"슈퍼맨")
print(movie_rank)
print(" ")

print("058")
nums = [1,2,3,4,5]
print(sum(nums))
print(" ")

print("059")
cook=["피자","김밥","만두","양념치킨","족발","피자","김치만두","쫄면","소시지","라면","팥빙수","김치전"]
print(len(cook))
print(" ")

print("060")
print(sum(nums)/len(nums))
print(" ")

print("102")
print("'print(3 == 5)'의 출력 결과를 예상하라.")
print("3과 5는 같지 않으므로 'False'")
print("결과",end=" => ")
print(3 == 5)
print(" ")

print("103")
print("'print(3 < 5)'의 출력 결과를 예상하라.")
print("3은 5보다 작으므로 'True'")
print("결과",end=" => ")
print(3 < 5)
print(" ")

print("104")
print("x = 4 \nprint(1 < x < 5)\n 다음 코드의 출력 결과를 예상하라.")
print("1 < 4 < 5 이므로 'True'")
print("결과",end=" => ")
x = 4
print(1 < x < 5)
print(" ")

print("105")
print('print ((3 == 3) and (4 !=3))\n다음 코드의 출력 결과를 예상하라.')
print("3 == 3이 참이고 4 != 3도 참이므로 'True'")
print((3 == 3) and (4 != 3))