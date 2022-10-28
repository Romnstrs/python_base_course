def square(num):
    return num**2


def gen(start,amount,func):
    i=0
    while i<amount:
        yield start
        start = func(start)
        i+=1


generator=gen(2,6,square)
print(list(generator))