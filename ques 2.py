def prime(a=1):
    i = 2
    c = 1
    number = a
    while(i * i < number or a != 1.0):
        while(a % i == 0):
            a = a / i
            c = i
        i = i + 1
    print("Largest prime factor of {} is {}".format(number, c))
    return None
prime(a=13195)
prime(a=600851475143)
