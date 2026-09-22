num: int=123456789
sum:int=0
def sumofdigit(num,sum:int=0):
    while(num>0):
        a=num%10
        sum=sum+a
        num=num//10
    return sum

print("Sum of digits of 123456789 is",sumofdigit(123456789))
print("Sum of digits of 112233445566778899 is",sumofdigit(112233445566778899))
a:int=123456789*987654321
print("Sum of digits of 123456789 ∗ 987654321. is",sumofdigit(a))


