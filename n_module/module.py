#import calc_add
# import calc.calc_sub
# import calc.calc_sub as sub
#from calc.calc_sub import sub
# from calc.calc import Calculator
#from calc.calc import *
import os
import sys

print(sys.path)
print(os.path.abspath(os.path.dirname(__file__)))
# print(sys.path.append(os.path.abspath(os.path.dirname(__file__))))

# if __name__ == '__main__':
#     print(calc_add.add(2, 3))
#     # print(calc.calc_sub.sub(10, 5))
#     # print(sub.sub(10, 5))
#     print(sub(10, 5))
#     print('=' * 20)
#     c = Calculator(10, 5)
#     print(c.add())
#     print(c.sub())