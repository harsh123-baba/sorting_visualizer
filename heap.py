import time




def heapify(arr, n, i, drawRectangle, delay):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        drawRectangle(arr, ['blue' if x == largest+1 else '#A7A9AC' for x in range(len(arr))]);
        # Heapify the root.
        time.sleep(delay);
        heapify(arr, n, largest, drawRectangle, delay)
 
# The main function to sort an array of given size
 
 
def heapSort(arr, drawRectangle, delay):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i, drawRectangle, delay)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        # drawRectangle(arr, ['blue' if x == i+1 else 'red' for x in range(len(arr))]);
        # time.sleep(delay);
        heapify(arr, i, 0, drawRectangle, delay)
 
    drawRectangle(arr, ['black' for x in range(len(arr))]);



