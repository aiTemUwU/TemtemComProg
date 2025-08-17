counter = 1
stop = False

maxLeftZig, maxRightZig = float('-inf'), float('-inf')
minLeftZig, minRightZig = float('inf'), float('inf')

while not stop:
    pair = input()
    if pair in ["Zig-Zag", "Zag-Zig"]:
        mode, stop = pair, True
    else:
        left, right = pair.split()
        left, right = int(left), int(right)
        
        if counter % 2 != 0:
            maxLeftZig = left if left > maxLeftZig else maxLeftZig
            maxRightZig = right if right > maxRightZig else maxRightZig
            
            minLeftZig = left if left < minLeftZig else minLeftZig
            minRightZig = right if right < minRightZig else minRightZig
        else:
            maxLeftZig = right if right > maxLeftZig else maxLeftZig
            maxRightZig = left if left > maxRightZig else maxRightZig
            
            minLeftZig = right if right < minLeftZig else minLeftZig
            minRightZig = left if left < minRightZig else minRightZig
    counter += 1

if mode == "Zig-Zag":
    minVal = minLeftZig
    maxVal = maxRightZig
else:
    minVal = minRightZig
    maxVal = maxLeftZig
    
print(f"{minVal} {maxVal}")
        