
import math
c=50
H=30
value = []
items=[x for x in input("Nhập giá trị của d: ").split(',')]
for D in items:
    value.append(str(int(round(math.sqrt(2*c*float(D)/H)))))
print (','.join(value))