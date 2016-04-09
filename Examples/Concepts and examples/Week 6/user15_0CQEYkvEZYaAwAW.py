n = 1000
numbers = range(2, n)
results = []

while numbers:
    c = numbers[0]
    results.append(c)
    for i in numbers:
        if i % c == 0:
            numbers.remove(i)

print len(results)