orders = [(14429, {('BSZ', 306): 14429}), (20569, {('SLZ', 306): 20569}), (16271, {('KKZ', 306): 16271}), (13201, {('RXZ', 306): 13201}), (24253, {('ZZZ', 306): 24253}), (21797, {('CTZ', 306): 21797})]

val = 1
import math
for cyclecount, _ in orders:
    val = math.lcm(val, cyclecount)
print(val)
