def armstrongnumbers(x):
    t=0
    s=0
    n=int(input("Enter the n value:"))
    while(x>0):
        a=x%10
        x=x//10
        s=(a**n)
        t+=s
        print(s)
    print(f"{t} is armstrong number")
armstrongnumbers(153)        
armstrongnumbers(370)
armstrongnumbers(9474)
