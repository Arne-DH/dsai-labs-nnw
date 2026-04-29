import numpy as np
import scipy.stats as stats

mean = 5
std = 1.5

x = 3

# stats.norm.sf(x, loc=mean, scale=std)

print(f"{stats.norm.cdf(3, loc=mean, scale=std):.2f}")


# 0.98

sum = 1/2 + 1/4 + 1/8 + 1/16 + 1/16

print(f"{sum:.2f}")