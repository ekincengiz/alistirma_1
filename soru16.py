x=int(input("bu sayı asal mıdır: "))
def asal(n):
    for i in range(2,n):
        if (n%i==0):
            return False
        return True
    
if (asal(x)):
    print(x,"sayısı asaldır.")
else:
    print(x,"sayısı asal değildir.")
        
