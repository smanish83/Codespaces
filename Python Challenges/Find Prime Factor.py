
def getPrimeFactor(number):
    factor = []
    division = 2
    # print(f'+==> Number is {str(number)} and division is {str(division)}')   
    while division <= number:
        # print(f'===> Number is {str(number)} and division is {str(division)}')       
        if number % division == 0:
            factor.append(division)
            number = number // division
        else:
            division = division + 1
            division = getPrimeNumberGreaterThan(division)
    
    return factor

def getPrimeNumberGreaterThan(prime_num):
    if prime_num <= 2:
        return prime_num
    
    if isPrime(prime_num):
        return prime_num
    else:
        return getPrimeNumberGreaterThan(prime_num + 1)

def isPrime(num):
    if num <=1 :
        return False
    else:
        is_prime=True
        for i in range(2, int(num**0.5)+1):
            if num % i ==0:
                is_prime = False
                break
        
        return is_prime
    
print(getPrimeFactor(630))
print(getPrimeFactor(13))
    