import time
# def merge(data, drawRectangle, delay):
#     if(len(data) > 1):
#         mid = len(data)//2
#         L = data[:mid];
#         R = data[mid : ];
#         merge(L, drawRectangle, delay);
#         merge(R, drawRectangle, delay)
#         i = j = k = 0;

#         while(i < len(L) and j < len(R)):
#             if(L[i] < R[j]):
#                 data[k] = L[i]
#                 i = i+1;

#             else:
#                 data[k] = R[j];
#                 j = j+1;
#             k += 1;

#         while(i < len(L)):
#             data[k] = L[i];
#             k += 1;
#             i += 1;
#         while(j < len(R)):
#             data[k] = R[j];
#             k += 1;
#             j += 1;
#         drawRectangle(data,[ 'blue' if x == j+1  else 'red' for x in range(len(data))])
#         time.sleep(delay);
#     drawRectangle(data, ['blue' for x in range(len(data))]);

 

def merge(arr, l, m, r, drawRectangle, delay):
    n1 = m - l + 1
    n2 = r - m
 
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    i = 0     
    j = 0     
    k = l     
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        drawRectangle(arr,[ 'blue' if x == l+1  else '#A7A9AC' for x in range(len(arr))])
        time.sleep(delay)
   
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        drawRectangle(arr,[ 'blue' if x == l+1  else '#A7A9AC' for x in range(len(arr))])
        time.sleep(delay)
    
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        drawRectangle(arr,[ 'blue' if x == l+1  else '#A7A9AC' for x in range(len(arr))])
        time.sleep(delay)
 
 
def mergeSort(arr, l, r, drawRectangle, delay):
    if l < r:

     
        m = l+(r-l)//2
        drawRectangle(arr,[ 'blue' if x == l+1  else '#A7A9AC' for x in range(len(arr))])
        time.sleep(delay)
        mergeSort(arr, l, m, drawRectangle, delay)
        drawRectangle(arr,[ 'blue' if x == l+1  else '#A7A9AC' for x in range(len(arr))])
        time.sleep(delay)
        
        mergeSort(arr, m+1, r, drawRectangle, delay)
        drawRectangle(arr,[ 'blue' if x == l+1  else '#A7A9AC' for x in range(len(arr))])
        time.sleep(delay)
        merge(arr, l, m, r,drawRectangle, delay)
        drawRectangle(arr,[ 'blue' if x == l+1  else '#A7A9AC' for x in range(len(arr))])
        time.sleep(delay)
    drawRectangle(arr, ['black' for x in range(len(arr))]);