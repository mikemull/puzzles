'''
Based on the idea that the lockers still open will be those corresponding to integers
with an odd number of factors.  That turns out to be any integer that is a square.
'''

def factors(n): return [i for i in range(1,n+1) if n % i == 0]

locker_states = [ len(factors(n)) % 2 == 1 for n in xrange(1,1001) ]

print 'There are {num_open} open lockers'.format(num_open=sum( 1 if x else 0 for x in locker_states ) )
print 'Locker 64 is {state}'.format(state='Open' if locker_states[63] else 'Closed')
