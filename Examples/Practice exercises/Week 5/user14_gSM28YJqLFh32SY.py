# Day to number problem

###################################################
# Student should enter code below

day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def day_to_number(day):
    pos = 0
    for i in range(len(day_list)):
        if day_list[i] == day:
            pos = i
    return pos

# You could also make used the list method index

###################################################
# Test data

print day_to_number("Sunday")
print day_to_number("Monday")
print day_to_number("Tuesday")
print day_to_number("Wednesday")
print day_to_number("Thursday")
print day_to_number("Friday")
print day_to_number("Saturday")

###################################################
# Sample output

#0
#1
#2
#3
#4
#5
#6
