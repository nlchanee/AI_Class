# # # # # # # # # # name = "BlockDMask"

# # # # # # # # # # if name == "BlockDMask" :
# # # # # # # # # #     print("이름이 맞습니다.")
# # # # # # # # # # else:
# # # # # # # # # #     print("이름이 다릅니다.")



# # # # # # # # # pocket = 1000

# # # # # # # # # if pocket == 1000:
# # # # # # # # #     print("복권 구매")
# # # # # # # # # elif pocket == 500:
# # # # # # # # #     print("껌 구매")
# # # # # # # # # else:
# # # # # # # # #     print("집이나 가자")


# # # # # # # # a = "사과"
# # # # # # # # b = "바나나"
# # # # # # # # c = "치즈"

# # # # # # # # if a == "사과" or b == "안바나나" :
# # # # # # # #     print("사과나 바나나입니다.")

# # # # # # # # if a == "사과" and "바나나" :
# # # # # # # #     print("사과이고 바나나입니다.")

# # # # # # # # if not b == "사과" :
# # # # # # # #     print("사과가 아니어야 여기 들어옵니다.")

# # # # # # # a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # # # # # # if 1 in a : 
# # # # # # #     print("a 리스트에 1이 포합되어있습니다.")
# # # # # # # if 10 in a :
# # # # # # #     print("a 리스트에 10이 포함되어 있습니다.")

# # # # # # P_class = "Z"
# # # # # # sel_amount = 79900

# # # # # # if P_class == 'A':
# # # # # #     sel_amount *= 0.7
# # # # # #     print(f"판매가는 {sel_amount}원입니다.")

# # # # # # elif P_class == 'Z':
# # # # # #     sel_amount *= 0.85
# # # # # #     print(f"판매가는 {sel_amount}원입니다.")
# # # # # #     print("판매가는 %f원입니다." % sel_amount)
# # # # # #     print("판매가는 %d원입니다." % sel_amount)


# # # # # x = 11

# # # # # if x < 10:
# # # # #     print("x는 10보다 작아")
# # # # # else:
# # # # #     print("x는 10보다 커")

# # # # # if x %2 == 0:
# # # # #     print("x는 짝수")
# # # # # else:
# # # # #     print("x는 홀수")

# # # # x = 8

# # # # if x<10 and x%2 == 0:
# # # #     print("x는 10보다 작으면서 짝수야.")
# # # # if x<10 and not x%2 ==0:
# # # #     print("x는 10보다 작으면서 홀수야.")
# # # # if not x<10 and x%2 == 0:
# # # #     print("x는 10보다 크면서 짝수야.")
# # # # if not x<10 and not x%2 == 0:
# # # #     print("x는 10보다 크면서 홀수야.")


# # # treeHit = 0

# # # while treeHit < 10:
# # #     treeHit = treeHit + 1
# # #     print("나무를 %d번 찍었습니다."%treeHit)
# # # if treeHit == 10:
# # #     print("나무 넘어갑니다.")

# # coffee = 10
# # money = 300
# # while money:
# #     print("돈을 받았으니 커피를 줍니다.")
# #     coffee = coffee-1
# #     print("남은 커피의 양은 %d개입니다."%coffee)
# #     if coffee == 0:
# #         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
# #         break

# while True:
#     print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")

i = 0
result1 = 0
while i < 100:
    i = i+2
    print("1번 방법 : {0}  {1}".format(i,result1))
    result1 = result1 + i

print("1번 방법 : {0}".format(result1))