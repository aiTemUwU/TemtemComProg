import numpy as np
import math

def p(x):
    logitX = -3.98 + 0.1*x[:, 0] + 0.5*x[:, 1]
    pX = 1/(1+math.e**(-logitX))
    return pX

exec(input().strip())