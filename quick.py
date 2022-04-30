import time

def partition(arr, low, high, drawRectangle, delay):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
            drawRectangle(arr, ['blue' if x == low + 1 else 'red' for x in range(len(arr))]);
            time.sleep(delay)
    
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return (i+1)
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
 
 
def quickSort(arr, low, high, drawRectangle, delay):
    if len(arr) == 1:
        return arr
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high, drawRectangle, delay)
        drawRectangle(arr, ['blue' if x == low + 1 else 'red' for x in range(len(arr))]);
        time.sleep(delay)
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1, drawRectangle, delay)
        drawRectangle(arr, ['blue' if x == low + 1 else 'red' for x in range(len(arr))]);
        time.sleep(delay)
        quickSort(arr, pi+1, high, drawRectangle, delay);
    drawRectangle(arr, ['blue' for x in range(len(arr))])
