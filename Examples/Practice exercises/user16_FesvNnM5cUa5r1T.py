def next(x):
    return (x ** 2 + 79) % 997

y = set([])
x = 1
for i in range(1000):
    print x
    y.add(x)
    x = next(x)    
    
print y
print len(y)