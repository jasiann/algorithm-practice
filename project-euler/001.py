'''
final = []

for i in range(1,1000, 2): 
    if i % 3 == 0 or i % 5 == 0: 
        final.append(i)

print(sum(final))
''' 

def sum_multiples(k, limit): 
    tlimit = (limit - 1 ) // k 
    
    final = k * (tlimit * (tlimit + 1 )) // 2
    return final 

print(sum_multiples(3, 1000) + sum_multiples(5,1000) - sum_multiples(15,1000))
