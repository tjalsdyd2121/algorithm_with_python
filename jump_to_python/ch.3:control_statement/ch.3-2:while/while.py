target = "Hello world"
str = ""
ch = "A"
leng = 0
while True:
  print(str + ch)
  if ch == target[leng]:
    str = str + ch
    leng += 1
    ch = "A"
  elif target[leng] == " ":
    ch = chr(31)
  ch = chr(ord(ch) + 1)

  if(str == target):
    break
  
  
# https://www.youtube.com/shorts/sV82aioUWS4?app=desktop
  