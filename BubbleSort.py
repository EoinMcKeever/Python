def countSwaps(a):
    n = len(a)
    counter = 0
    for i in range(n-1):
        for j in range(0,n -i - 1):
            if a[j] > a[j + 1]:
                counter+=1
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp 
    print("Array is sorted in "+ str(counter)+ " swaps.")
    print("First Element: "+str(a[0]))
    print("Last Element: "+str(a[-1]))
  