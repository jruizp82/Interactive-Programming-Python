def next(x):
    return (x ** 2 + 79) % 997

y = set([])
x = 1
for i in range(1000):
    print x
    x = next(x)
    y.add(x)
    
print y
print len(y)