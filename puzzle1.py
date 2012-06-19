import itertools

def check(x,level,n):
     if level == 1:
             print(n)
     else:
             if x % level == 0:
                     check( x // 10, level-1, n)


start_numbers = [int(''.join(n)) for n in itertools.permutations("123456789")]

for n in start_numbers:
    check(n, 9, n)

