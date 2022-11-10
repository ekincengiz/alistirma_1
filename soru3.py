import math

toplam=1
faktoriyel=1
for i in range(1,100):
    faktoriyel=faktoriyel*i
    toplam=toplam+(1/faktoriyel)

print(toplam)
print(math.e)
