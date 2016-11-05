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
