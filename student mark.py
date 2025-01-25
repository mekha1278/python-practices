tam=int(input("Enter Tamil mark"))
eng=int(input("Enter english mark"))
mat=int(input("Enter the maths mark"))
sci=int(input("Enter the science mark"))
soc=int(input("Enter the social mark"))
total=tam+eng+mat+sci+soc
percentage=total/5
print(total)
print(percentage)
if((total>=0)&(total>=500)):
    print("invalid")
elif(total>=499)&(total>=400):
    print("A")
elif( total>399)&(total>=300):
    print("B")
elif( total>=299)&(total>=200):
    print("C")
else:
    print("D")            