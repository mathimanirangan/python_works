headline= "Produce the result we need."
def result(arg1,arg2):
    """
    %s
    It is really good you should use it.
    """
    return arg1 + arg2

result.__doc__ %= headline

help(result)
