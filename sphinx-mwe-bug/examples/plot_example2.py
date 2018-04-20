"""
Example 2
=========

This is example 2.
"""

import sys
sys.path.append('../mymodule')
import module

import matplotlib.pyplot as plt

m = module.MyClass()
m.set_attribute("yumulu")
plt.xlabel(m.get_attribute())
module.myfunction("yada da")
plt.show()
