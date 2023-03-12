import time

def for_loop_function(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def sum_with_while_loop(n):
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1
    return sum

# Measure execution time for for_loop_function
for n in [10, 100, 1000, 10000, 100000]:
    start_time = time.time()
    result = for_loop_function(n)
    end_time = time.time()
    time_total = end_time - start_time
    print(f"n={n}: for loop time={time_total:}, Sum={result}, Time_total={time_total}")

# Measure execution time for sum_with_while_loop
for n in [10, 100, 1000, 10000, 100000]:
    start_time = time.time()
    result = sum_with_while_loop(n)
    end_time = time.time()
    time_total = end_time - start_time
    print(f"n={n}: while loop time={time_total}, Sum={result}, Time_total={time_total}")
