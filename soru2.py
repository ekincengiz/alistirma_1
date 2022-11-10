import math

toplam=0
for i in range(1,10000000,1):
    toplam=toplam+(1/(i*i))

pi=math.sqrt(6*toplam)

print(pi)
