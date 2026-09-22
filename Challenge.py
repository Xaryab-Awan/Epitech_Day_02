# a=20
# while(True):
#     check=True
#     for i in range (1,20+1):
#         if(a%i !=0):
#             check=False
#             break
#     if(check):
#         break
#     a=a+20
# print("Answer",a)

print("THIS APPROACH IS TAKING AALOT OF TIME")

def gcd(a,b):
    while b!=0:
     a,b= b,a%b
    return a
def lcm(a,b):
    lcm=a*b//gcd(a,b)
    return lcm

def smallest_divisible(num):
    ans=1
    for i in range(1,num+1):
        ans=lcm(ans,i)
    return ans

num1=int(input("Enter the range: "))
print("Smallest divisible number from 1 to",num1,"is",smallest_divisible(num1))
        
