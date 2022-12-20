
def countingValleys(steps, path):
    count = 0
    valleys = 0
    temp = 0
    for i in range(steps):
        if path[i] == "U":
            count += 1
        else:
            count -= 1
        if count < 0:
            temp = 1
        if temp == 1 and count >= 0:
            temp = 0
            valleys += 1
    return valleys                  
        
    # Write your code here