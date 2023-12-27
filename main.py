def even_odd_generator(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"
        if i % 3 == 0 and i % 5 != 0:
            yield "Fizz"
        if i % 3 != 0 and i % 5 == 0:
            yield "Buzz"
        if i % 3 != 0 and i % 5 != 0:
            yield i


a = even_odd_generator(18)
for i in a:
    print(i)
