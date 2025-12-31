

def ft_filter(fun,iterab):
    '''filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.'''
    arr = []
    for i in iterab:
        if fun(i):
            arr.append(i)
    it = iter(arr)
    return it