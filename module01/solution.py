def f_c(x):
    """
        Always return 4
    :param x: any parameter
    :return: 4
    """
    return 4

def f_x(x, a, b):
    return a*x + b

def sum(x):
    s = f_x(x, 1, 1)
    s += f_x(x, 2, 2)
    s += f_x(x, 3, 3)
    return s
