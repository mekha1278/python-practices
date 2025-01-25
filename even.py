# def odd():
#     for i in range(1,100):
#         if(i%2!=0):
#             print(i)
# odd()

# def table():
#     for i in range(1,100):
#         if(i%5==0):
#             print(i)
# table()
# def add(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     print(sum)
# add(10)
# n=nums[0]

# nums=[1,2,3,4,5,6,7,8]
# for i,j in enumerate(nums):
#     print(f"index : {i} , value : {j}")

# for i in range(5):
#     print("*"*5)
# for i in range(5):
#     print("*")
#     for j in range(5):
#         print("")
# print("*"*5)
# print("*"*5)
# print("*"*5)
# print("*"*5)
# print("*"*5)
# for i in range(0,5):
#     for j in range(0,5):
#         print("*",end="")
#     print()
# n=5
# for i in range(n):
#     s=""
#     for j in range(n):
#         s+="*"
#     print(s)
# n=5
# for i in range(n):
#     s=""
#     for j in range(n-i):
#         s+="*"
#     print(s)

# n=5
# for i in range(n):  
#     s=" "
#     for j in range(n-1-i):
#         s+=" "
#     for k in range(i+1):
#         s+="*"
#     print(s)
# n=5
# for i in range(n):
#     s=" "
#     for j in range(n-1-i):
#         s+=" "
#     for k in range(2*i+1):
#         s+="*"
#     print(s)
# for i in range(1,6):
#     s=""
#     for j in range(1,6):
#         s+=""
#     print(s)    
# n=5
# for i in range(1,n+1):
#     s=" "
#     for j in range(1,n+1):
#         s+=str(j)
#     print(s)    
# # n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end=" ")
#     print()
# n=
# for i in range(n+1):
#     s=" "
#     for j in range(n+1):
#         s+=str(j)
#     print(s) 
# n=5
# for i in range(n):
#     s=""
#     for j in range(n):
#         s+=i+1
#     print(s)
# n=5
# for i in range(1,n+1):
#     if()
#     s=""
#     for j in range(1,i+1):
#         s+=str(j)
#     print(s) 
# n=5
# for i in range(n):
#     s=""
#     for j in range(n):
#         s+=i+1
#     print(s)
# n=5
# for i in range(n+1):
#     s=" "
#     for j in range(n+1):
#         s+=str(j)
#     print(s)
# n=5
# value=0
# for i in range(1,n+1):
#     sum=" "
#     for j in range(1,i+1):
#         value+=1
#         sum+=str(value)
#         sum+=" "
#     print(sum)

# n=5
# for i in range(0,n):
#     k=" "
#     for j in range(1,n+1):
#         if(i+j<=n):
#             k+=str(i+j)
#             k+=" "
#         else:
#             k+=str(i+j-n)
#             k+=" "
#     print(k)

# n=4
# for i in range(0,7):
#     k=" "
#     for j in range((2*n)-1):
#         top=i
#         bottom=j
#         left=(2*n-2)-i
#         right=(2*n-2)-j
#         k+=str(n-min(min(top,right),min(left,bottom)))
#     print(k)

# n=5
# for i in range(0,n):
#     s=""
#     for j in range(0,n-1-i):
#         s+="_"
#     for k in range(i+1,0,-1):
#         s+=str(k)
#     print(s)

   
# n=5
# for i in range(1,n+1):
#     s=" "
#     for j in range(1,i+1):
#         s+=str(j)
#     print(s)

sum=8
n=4
for i in range(1,n+1):
    s=" "
    sum+=i
    val=sum
    for j in range(n-i):
        s+="_"
    for k in range(i):
        s+=str(val)+" "
        val-=1
    print(s)

