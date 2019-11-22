# from typing import Any


def num_add(a, b):
    return a + b

def num_sub(a, b):
    return a - b

def num_mul(a, b):
    return a * b

def num_div(a, b):
    return a / b

def num_floor(a, b):
    return a // b

def num_rem(a, b):
    return a % b


IS_TRUE = True

IS_FALSE = False

PANCAKE_INGREDIENTS = {
    "flour": 2,
    "eggs": 4,
    "milk": 200,
    "butter": False,
    "salt": 0.001
}

def ingredient_exists(ingr, dict):
    return ingr in dict

def fatten_pancakes(dict):
    fatten = dict.copy()
    fatten['eggs'] = 6
    fatten['butter'] = True
    return fatten

def add_sugar(dict):
    sweet = dict.copy()
    sweet['sugar'] = 7
    return sweet

def remove_salt(dict):
    no_salt = dict.copy()
    del no_salt['salt']
    return no_salt


FIBONACCI_NUMBERS = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

def add_fibonacci(lst):
    next = lst[-1] + lst[-2]
    lst.append(next)
    return lst

def fib_exists(lst, n):
    return n in lst

def which_fib(lst, n):
    return lst.index(n) + 1
