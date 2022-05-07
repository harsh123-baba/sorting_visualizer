
# def merge(arr, l, m, r):
#     n1 = m - l + 1
#     n2 = r - m
 
#     L = [0] * (n1)
#     R = [0] * (n2)
 
#     for i in range(0, n1):
#         L[i] = arr[l + i]
 
#     for j in range(0, n2):
#         R[j] = arr[m + 1 + j]
 
#     i = 0     
#     j = 0     
#     k = l     
 
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1

   
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1

    
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1
        
 
 
# def mergeSort_Complex(arr, l, r):
#     if l < r:

     
#         m = l+(r-l)//2

#         mergeSort_Complex(arr, l, m)

        
#         mergeSort_Complex(arr, m+1, r)

#         merge(arr, l, m, r)

# MergeSort in Python


def mergeSort_Complex(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort_Complex(L)
        mergeSort_Complex(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1