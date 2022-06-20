import time

def bubble_sort(data, drawRectangle, delay):
    for i in range(len(data) -1):
        for j in range(len(data) -1 ):
            if(data[j] > data[j+1]):
                temp = data[j];
                data[j] = data[j+1];
                data[j+1] = temp;
                drawRectangle(data, ['blue' if x == j+1 else '#A7A9AC' for x in range(len(data))])
                time.sleep(delay)
            
    drawRectangle(data, ['black' for x in range(len(data))])
