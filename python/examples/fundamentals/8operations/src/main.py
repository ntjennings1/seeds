""" Native Import. """
import math

""" Gathers the number to perform mathematical operations on.

@return num : The input
@rtype num : str
"""
def get_num():

    num = input('Enter a positive number greater than zero (e to exit): ')
    return num

""" Repetitively perform mathematical operations on a number.

@returns null
"""
def operations():

    go = True

    while go:
        num = get_num()
        
        if num.strip() == 'e':
            go = False
        else:
            num = int(num)

            sqrt = math.sqrt(num)
            cbrt = math.cbrt(num)
            factorial = math.factorial(num)
            log2 = math.log2(num)
            log10 = math.log10(num)

            print()
            print('The square root of ', num, ' is: ', sqrt)
            print('The cube root of ', num, ' is: ', cbrt)
            print(num, ' factorial is: ', factorial)
            print('log2(', num, ') is: ', log2)
            print('log10(', num, ') is: ', log10)
        
""" Runs the operations function. """
operations()