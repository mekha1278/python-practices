# print("enter the current condition for meghna")
# meghna=str(input())
# if(meghna=="died"):
#     print("\nsurya meets priya")
# else:
#     print("\nsurya weds meghna")
num=int(input("Enter the value"))
for i in range(1,num+1):
    if(i*i==num):
        print(True)
        break
    elif(i*i>=num):
        print(False)
        break
