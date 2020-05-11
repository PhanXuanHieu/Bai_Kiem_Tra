lines = []
while True:
   s = input(' Nhập chuỗi:')
   if s:
      lines.append(s.upper())
   else:
      break
for ch in lines:
    print (ch)