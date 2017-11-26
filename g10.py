"""
My super-lame way to find the answer to the Google 1,1,5,8 puzzle.

The idea is that you must use these numbers each once, and you can use the operators +,-, /, * and (), to calculate
the number 10.

"""
import operator
from itertools import permutations, combinations_with_replacement


def calc10(inputs, op_ord, ops):
    """
    There are only 5 possible binary trees corresponding to the possible groups of operations, so i
    just enumerate them here
    """
    a, b, c, d = inputs
    o1, o2, o3 = op_ord

    return (
        (o1(o2(a, b), o3(c, d)), '({a}{op2}{b}){op1}({c}{op3}{d})'.format(a=a,op2=ops[o2],b=b,op1=ops[o1],c=c,op3=ops[o3],d=d)),
        (o1(a, o2(o3(b, c), d)), '{a}{op1}(({b}{op3}{c}){op2}{d})'.format(a=a,op2=ops[o2],b=b,op1=ops[o1],c=c,op3=ops[o3],d=d)),
        (o1(a, o2(b, o3(c, d))), '{a}{op1}({b}{op2}({c}{op3}{d}))'.format(a=a,op2=ops[o2],b=b,op1=ops[o1],c=c,op3=ops[o3],d=d)),
        (o1(o2(a, o3(b, c)), d), '({a}{op2}({b}{op3}{c})){op1}{d}'.format(a=a,op2=ops[o2],b=b,op1=ops[o1],c=c,op3=ops[o3],d=d)),
        (o1(o2(o3(a, b) ,c), d), '(({a}{op3}{b}){op2}{c}){op1}{d}'.format(a=a,op2=ops[o2],b=b,op1=ops[o1],c=c,op3=ops[o3],d=d)),
    )


def search_for_10():
    """ Look for combination of numbers and operators that will give you 10"""
    inputs = set(permutations([1, 1, 5, 8]))

    ops = {operator.add: '+', operator.sub: '-', operator.mul: '.', operator.truediv: '/'}
    op_orders = set(combinations_with_replacement(ops.keys(),3))

    # Try all possible permuations of the numbers
    for inp in inputs:
        i = 0
        for opord in op_orders:
            # Try all possible 3-member sets of the 4 operators
            for opset in set(permutations(opord)):
                # Try all permutations of the operators
                try:
                    x = calc10(inp, opset, ops)
                    if any([t == 10 for t,e in x]):
                        print(list(ops[p] for p in opset))
                        for t,e in x:
                            i += 1
                            print(i, t, e)
                except ZeroDivisionError:
                    pass


search_for_10()