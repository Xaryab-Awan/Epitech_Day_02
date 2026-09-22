def pie(a):
    if a>=1000:
        return a**2/6
    
    return a**2/ (6+ pie(a+2))

val=(3+pie(1))
val=val-int(val)
val=int(val*1000000)/1000000
print("First 6 digit of pie are",val)

