# x*x = 1_2_3_4_5_6_7_8_9_0
# 

from math import sqrt
from re import match

print sqrt(1020304050607080900)
print sqrt(1929394959697989990)

x = 1389010000
while x < 1389026623:
    if match(r'1.2.3.4.5.6.7.8.9.0', '%d' % x**2):
        print x, '@'
        break
    x += 10
    print x