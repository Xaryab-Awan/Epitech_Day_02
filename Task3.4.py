def extractecimal(a):
    return (a-int(a))

print(f"Decimal Part is:{extractecimal(12.24):.2f}")

print(f"Decimal Part is:{extractecimal(424242.8412):.2f}")