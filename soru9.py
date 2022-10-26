for i in range(1,1000):
    a=str(i)+"000"
    if int(a[0])+int(a[1])+int(a[2])<9:
        print(i,end=' ')
