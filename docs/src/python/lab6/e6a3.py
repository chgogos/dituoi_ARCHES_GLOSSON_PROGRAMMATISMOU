def running_totals(numbers):
    total = 0
    for n in numbers:
        total += n
        yield total



numbers = [4, 7, 2, 10]

for value in running_totals(numbers):
    print(value)
