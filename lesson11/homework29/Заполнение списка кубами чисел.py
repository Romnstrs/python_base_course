def generate_cube_numbers(num:int):
    i=2
    while i**3<num:
        yield i**3
        i+=1


gen=generate_cube_numbers(1001)
print(next(gen))
print(next(gen))
print(list(gen))





