limit = 4000000
running_total = 0 

a = 1
b = 2

while a <= limit:
    if a % 2 == 0: 
        running_total += a 
    a,b = b, a + b 
print(running_total)
