import itertools
from operator import mul

def primefactors(x):
    ''' Find the prime factors of an integer '''
    facs=[]
    divisor=2
    while divisor <= x:
        if x % divisor == 0:
            x /= divisor
            facs.append(divisor)
        else:
            divisor += 1
    return facs

def nfactors(s):
    ''' Number of factors.  Seriously. '''
    return reduce( mul, (len(list(g))+1 for k,g in itertools.groupby(primefactors(s))) )

def triangle_num():
    ''' Good ol' fashioned generator '''
    x = n = 1
    while True:
        yield x, n
        n += 1
        x += n

num_factors = 0
tn = triangle_num()
tn.next()
while num_factors <= 500:
    x, n = tn.next()
    num_factors = nfactors(x)
print x, n, num_factors

