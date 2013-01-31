'''
Create a matrix where the numbers are arranged in a spiral
'''
import numpy as np

def spiral(n,start):
    ''' Generate the indexes of the spirals path '''
    x, y = start

    if n < 1:
        return []
    elif n==1:
        return [(start[0], start[1])]
    else:
        path = [(start[0], start[1] + i) for i in xrange(0,n)] + \
               [(start[0] + i, start[1] + n-1) for i in xrange(1,n)] + \
               [(start[0] + n-1, start[1] + n-i-1) for i in xrange(1,n)] + \
               [(start[0] + n-i-1, start[1] ) for i in xrange(1,n-1)]

    return path + spiral(n-2, (start[0]+1,start[1]+1))


def spiral_array(n):
    ''' Map the sequence from 1 to n into the matrix '''
    s_array = np.zeros((n,n))
    spiral_path = spiral(n,(0,0))
    for i in range(n*n):
        s_array[ spiral_path[i] ] = i+1

    return s_array


if __name__ == '__main__':
    print spiral_array(4)
