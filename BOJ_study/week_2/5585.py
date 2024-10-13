pay = int(input())
payback = 1000 - pay # 620
money = [500, 100 ,50, 10 , 5, 1]
index = 0
answer = 0
while payback != 0 : 
  answer += (payback // money[index]) # 1 ->
  payback = (payback % money[index]) # 
  #print(payback)
  index+=1

print(answer)