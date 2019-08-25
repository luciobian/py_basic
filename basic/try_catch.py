def div42by(divideBy):
    try:
        result = 42/divideBy
        return result
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

print(div42by(20))
print(div42by(10))
print(div42by(0))

