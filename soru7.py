a=0
for i in range (100,1000):
    b=str(i)
    c = b[0]
    d= b[1]
    e= b[2]
    if int(c)+int(d) == int(e):
        a+=1
        print(b)

print("toplam sonuç sayısı:", a)

