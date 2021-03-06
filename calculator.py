import re
import sys
from math import factorial

ops = "(\+|\-|\*|\/|\!|\^|nck)"
nums = "(0|([1-9]0*\d*)*)(\.\d*){0,1}"
opre = re.compile("^" + ops + "$")
numre = re.compile("^" + nums + "$")

def is_num(n):
    return numre.match(n) != None

def is_op(n):
    return opre.match(n) != None

def get_res(token, nums):
    try:
        res = nums.pop()
    except:
        print(str.format('Error: Operator ”{0}" without operand(s) found.', token))
        sys.exit(0)
    if token == '+':
        for n in nums:
            res = res + n
        nums[:] = []
    elif token == '*':
        for n in nums:
            res = res * n
        nums[:] = []
    elif token == '-':
        if len(nums) == 0:
            res = -res
        else:
            for n in nums:
                res = res - n
            nums[:] = []
    elif token == '/':
        for n in nums:
            res = res / n
        nums[:] = []
    elif token == '!':
        res = factorial(res)
    elif token == '^':
        for n in nums:
            res = res**n
        nums[:] = []
    elif token == 'nck':
        try:
            k = nums.pop()
            res = factorial(res) / (factorial(k) * factorial(res - k))
        except:
            print('Error. N choose K needs two arguments.')
            sys.exit()
    return res

def calculate(argument):
    stack = []
    input = argument.lstrip().rstrip().split(" ")
    for token in reversed(input):
        if is_num(token):
            stack.append(float(token))
        elif is_op(token):
            res = get_res(token, stack)
            stack.append(res)
        else:
            print(str.format("An error occurred. Token \"{0}\" is neither an operator or number.", token))
            sys.exit(0)
    return stack.pop()
