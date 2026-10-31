def prime_factor_max(n): 
    running_sum = n 
    final = []
    inc = 2
    
    while running_sum != 1: 
        if running_sum % inc == 0: 
            while running_sum % inc == 0:
                running_sum = running_sum // inc
                final.append(inc)
                if running_sum == 1: 
                    break
        inc += 1
    return final[-1]
print(prime_factor_max(600851475143))      
