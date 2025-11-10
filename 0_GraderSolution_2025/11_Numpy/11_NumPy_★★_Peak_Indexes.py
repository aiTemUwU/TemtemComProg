import numpy as np

def peak_indexes(x):
    mainX = np.append(np.array([-np.inf]), x)
    mainX = np.append(mainX, np.array([-np.inf]))

    rightShiftX = (np.append(np.array([-np.inf]), mainX))[:-1]
    leftShiftX = (np.append(mainX, np.array([-np.inf])))[1:]

    peak = np.where(mainX > rightShiftX, mainX, 0)
    peak = np.where(peak > leftShiftX, peak, 0)

    filteredPeak = peak[1:-1]
    filteredPeak[0] = 0
    filteredPeak[-1] = 0

    return np.where(filteredPeak != 0)[0]

def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else: print("No peaks")

exec(input().strip())