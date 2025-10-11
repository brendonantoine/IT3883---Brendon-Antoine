import time

def current_milli_time():
    return round(time.time() * 1000)

def is_prime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    # Only check up to sqrt(x)
    limit = int(x ** 0.5) + 1
    for i in range(3, limit, 2):  # check only odd numbers
        if x % i == 0:
            return False
    return True

rs = 1000
re = 40000

start = current_milli_time()
for i in range(rs, re):
    if is_prime(i):
        print(i, "is prime")
end = current_milli_time()

print((re - rs), "numbers searched in", end - start, "milliseconds")
