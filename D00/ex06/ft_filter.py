

def ft_filter(fun,iterab):
    '''filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.'''
    if fun is None:
        return iter([item for item in iterab if item])
    return iter([item for item in iterab if fun(item)])