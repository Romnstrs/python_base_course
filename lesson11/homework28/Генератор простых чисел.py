def prime_generator(num:int):
    i = 2
    j = 2
    lst = []
    while i <= num:
        while j<=i and i%j!=0:
            j+=1
        if i==j:
            lst.append(j)
            yield j
        i+=1
        j=2



generator=prime_generator(100)
print(next(generator))
print(next(generator))
print(list(generator))


