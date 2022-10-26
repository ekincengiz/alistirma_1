def asal(n):
    for i in range (2,n):
        if(n%i==0):
            return False
        return True

for i in range (10000,100000):
    if(asal(i)):
       print(i)
