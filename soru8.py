a=0
for i in range (100,1000,2):
    b=str(i)
    if b[0]==b[1] or b[1]==b[2] or b[0]==b[2]:
        a=a+1

print(a)
