pie=0
for i in range(100000):
    pie+=(-1)**i /(2*i+1)
pie*=4
pie=pie-int(pie)
ans=int(pie*1000000)/1000000
print("first 6 digit of pie are",ans)