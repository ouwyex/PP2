from functools import reduce
import time
import math

def multiply_list(lst):
    return reduce(lambda x, y: x * y, lst)

def count_case(s):
    return sum(map(str.isupper, s)), sum(map(str.islower, s))

def is_palindrome(s):
    return s == s[::-1]

def delayed_sqrt(n, delay):
    time.sleep(delay / 1000)
    return math.sqrt(n)

def all_true(tpl):
    return all(tpl)

print(multiply_list([1, 2, 3, 4]))  
print(count_case("Hello World"))     
print(is_palindrome("madam"))        
print(delayed_sqrt(25100, 2123))     
print(all_true((True, True, False)))
