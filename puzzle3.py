

def primefactors(x):
    factorlist=[]
    loop=2
    while loop<=x:
        if x%loop==0:
            x/=loop
            factorlist.append(loop)
        else:
            loop+=1
    return factorlist

def nfactors(s):
    return reduce( mul, (len(list(g))+1 for k,g in itertools.groupby(primefactors(s))) )

def factors(n): return [i for i in range(1,n+1) if n % i == 0]

def triangle_num():
    x = 1
    n = 1
    while True:
        yield x, n
        n += 1
        x += n

def find_answer():
    num_factors = 0
    tn = triangle_num()
    tn.next()
    while num_factors <= 500:
        x, n = tn.next()
        num_factors = nfactors(x)
    print x, n, num_factors
