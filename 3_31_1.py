#1
price_list1 = [32100,32150,32000,32500]
i = 0
while i<4 :
    print(i,end =" ")
    print(price_list1[i])
    i = i+1

print(" ")
#2
price_list2 = [32100,32150,32000,32500]
j = 0
k = 100
while j < 3 :
    print(k, end = " ")
    print(price_list2[j+1])
    k = k+10
    j = j +1

print(" ")
#3
for d in range(2002,2050):
    if(d%4==0):
        print(d-2)

print(" ")
#4
for a in range(0,9):
    print(a*0.1)

print(" ")
#5
ticker = "btc_krw"
print(ticker.upper())

print(" ")
#6
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))

print(" ")
#7
a = "hello world"
print(a.split())

print(" ")
#8
date = "2020-05-01"
date_modify = date.split("-")
print(date_modify[0],"년",date_modify[1],"월",date_modify[2],"일")
#print(date_modify)

print(" ")
#9
상장주식수 = "5,969,782,550"
data = 상장주식수.replace(",","")
print(data)

print(" ")
#10
a = "hello world"
print(a.split())

print(" ")
#11
price = ['20180728', 100, 130, 140, 150, 160, 170]

print(" ")
#12
nums = [1,2,3,4,5,6,7,8,9,10]
for c in range(0,9):
    if(nums[c]%2 == 0):
        print(nums[c],end=" ")

print(" ")
#13
리스트  = [3,100,23,44]
for b in range(0,3):
    if(리스트[b]%3 == 0):
        print(리스트[b])