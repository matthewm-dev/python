#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 19 10:29:49 2025

@author: matthew
"""

# Write a program that does the following in order:
# 1. Asks the user to enter a number “x”
# 2. Asks the user to enter a number “y”
# 3. Prints out number “x”, raised to the power “y”.
# 4. Prints out the log (base 2) of “x”.

import numpy

print('enter a number “x”:')
x = int(input())
print('enter a number “y”:')
y = int(input())
power = x**y
log = numpy.log2(x)
print('“x” raised to the power “y”:', power)
print('log (base 2) of “x”:', log)