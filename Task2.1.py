print("************ FIRST PART ***************")
num1=0
n=0
for i in range(9):
    n=n*10+1
    num1+=n    

print("Answer without power:" , num1)
j=2
for i in range(4):
    print("Answer with power:", j, pow(num1, j))
    j=j+1


print("************ NEXT PART ***************")
num2=0
n=0
for i in range(10):
    n=n*10+1
    num2+=n    

print("Answer without power:" , num2)
j=2
for i in range(4):
    print("Answer with power:", j, pow(num2, j))
    j=j+1
