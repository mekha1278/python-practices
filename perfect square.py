num=int(input("Enter the value"))
for i in range(1,num+1):
    if(i*i==num):
        print(True)
        break
    elif(i*i>=num):
        print(False)
        break
