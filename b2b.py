print("Welcome to b2b converter! Provide any two numbers with an indicator (one of any of the following ten letters at the end of the number to identify which numerical system the number should be recognized as part of).\n indicators = {\n b: binary, 'base 2';\n t: ternary, 'base 3';\n q: quaternary, 'base 4';\n p: quinary, 'base 5';\n h: hexary, 'base 6';\n s: septimal, 'base 7';\n o: octal, 'base 8';\n n: nonary, 'base 9';\n d: decimal, 'base 10'\n}")

indicators = {'b': 2, 't': 3, 'q': 4, 'p': 5, 'h': 6, 's': 7, 'o': 8, 'n': 9, 'd': 10}
dig = [f'{m}' for m in range(10)]

def floor_log(num, base):
    a = 0
    while num >= base:
        num /= base
        a += 1
    return a

def baseconverter(nums):
    I1 = nums[0][-1]
    I2 = nums[1]

    nums[0] = nums[0][:-1]
    if not {I1, I2}.issubset(indicators.keys()):
        return TypeError, "Couldn't recognize indicator:", indicators

    if I1 in list(indicators.keys())[:-1]:
        if I2 in list(indicators.keys())[:-1]:
            return ten_to_b(b_to_ten(nums[0], I1), I2)

        return b_to_ten(nums[0], I1)
    
    return ten_to_b(nums[0], I2)
    

def b_to_ten(n, base_from):
    bf = indicators[base_from]

    s = 1
    if n[0] == '-':
        n = n[1:]
        s =-1

    if n == '0': return 0
    for j in n:
        if j not in dig[:bf]: return TypeError, "Couldn't recognize number; check for any typos" 

    l = len(n)
    bint = 0
    for i in range(l):
        bint += s*int(n[i])*(bf**(l-(i+1)))

    return f'{bint}'

def ten_to_b(n, base_to):
    bt = indicators[base_to]
    
    s = 1
    if n[0] == '-':
        n = n[1:]
        s = -1

    for i in n:
        if i not in dig: return TypeError, "Couldn't recognize number; check for any typos"

    nint = int(n)
    if nint == 0: return '0'
    
    l = floor_log(nint, bt)
    b = [0]*(l+1)
    bint = 0

    while nint > 0:
        p = floor_log(nint, bt)
        nint -= bt**p
        j = -p-1

        b[j] = 1
        bint += s*(10**p)
    
    return f'{bint}'

while True:
    num = input("Your number (must end with an indicator for the base) >> ")
    bt = input("The base in which your number should be represented (one-letter indicator) >> ")

    nums = [num, bt] # number w/ indicator + single letter indicating base_to.

    print(baseconverter(nums=nums))