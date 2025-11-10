import numpy as np

def toCelcius(f):
    celcius = (5/9) * (f-32)
    return celcius

def BMI(wh):
    weight = wh[:, 0]
    height = wh[:, 1]/100

    return weight/(height**2)

def distanceTo(p, Points):
    xp, yp = p[0], p[1]
    xPoints, yPoints = Points[:, 0], Points[:, 1]

    return np.sqrt((xp-xPoints)**2 + (yp-yPoints)**2)

exec(input().strip())