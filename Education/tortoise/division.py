
divisor = 15
target = 90
mul = 1


while True:
    product = mul * divisor
    diff = target - product
    if diff > 0:
        mul = mul + 1
    else:
        break

result = mul
print('result is ', result)

