import time


def selection_sort(data, drawRectangle, delay):
    for i in range(len(data)):
        min = i;
        for j in range(i+1, len(data)):
            if(data[j] < data[min]):
                min = j;
                drawRectangle(data, ['blue' if x == j+1 else 'red' for x in range(len(data))]);
                time.sleep(delay)
        temp = data[i];
        data[i] = data[min];
        data[min] = temp;

        drawRectangle(data, ['blue' if x == i+1 else 'red' for x in range(len(data))]);
        time.sleep(delay)
    drawRectangle(data, ['blue' for x in range(len(data))]);



