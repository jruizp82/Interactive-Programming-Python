slow_wumpuses = 1000
fast_wumpuses = 1

year = 0

while fast_wumpuses < slow_wumpuses:
    slow_wumpuses *= 2
    slow_wumpuses = slow_wumpuses - slow_wumpuses*0.4
    fast_wumpuses *= 2
    fast_wumpuses = fast_wumpuses - fast_wumpuses*0.3
    year += 1
    #if fast_wumpuses > slow_wumpuses:
    #    break
print year