import tkinter as tk
from tkinter import ttk
from bubbleSort import bubble_sort
from merge import mergeSort
from selection_sort import selection_sort
from quick import quickSort
from heap import heapSort
from tkinter import *
import random
root = tk.Tk();
root.title("Sorting Visualizer");
root.geometry("1020x800")
root.config(bg= "pink")




select_algorithm = tk.StringVar()
arr = [];


def genrate_array():
    global arr;
    lowest = int(lowest_entry.get());
    highest = int(highest_entry.get());
    size = int(size_entry.get());
    arr = [];

    for i in range(size):
        arr.append(random.randrange(lowest, highest+1));

    drawRectangle(arr,['red' for x in range(len(arr))]);


def drawRectangle(arr, colorArray):
    barWindow.delete('all')
    canvas_height = 500;
    canvas_width = 730;
    bar_width = canvas_width / (len(arr) + 1);
    border_offset = 30
    spacing = 10;
    normalized_array = [i / max(arr) for i in arr];
    for i, height in enumerate(normalized_array):
        x0 = i*bar_width + border_offset + spacing;
        y0 = canvas_height - height * 340

        x1 = (i+1) * bar_width + border_offset;
        y1 = canvas_height;

        barWindow.create_rectangle(x0, y0, x1, y1, fill = colorArray[i])
        barWindow.create_text(x0+2, y0, anchor=SW, text = str(arr[i]));

    root.update_idletasks()

def sorting():
    # global arr
    # merge(arr, drawRectangle, sort_speed.get());
    # bubble_sort(arr, drawRectangle, sort_speed.get());
    # # selection_sort(data, drawRectangle, sort_speed.get());
    if select_algorithm.get() == 'Merge Sort':
        # global arr
        mergeSort(arr,0, len(arr)-1,  drawRectangle, sort_speed.get());
    
    elif select_algorithm.get() == 'Bubble Sort':
        # global arr
        bubble_sort(arr, drawRectangle, sort_speed.get());
    
    elif select_algorithm.get() == 'Quick Sort':
        quickSort(arr, 0, len(arr)-1, drawRectangle, sort_speed.get());
    
    elif select_algorithm.get() == 'Selection Sort':
        selection_sort(arr, drawRectangle, sort_speed.get());

    elif select_algorithm.get() == 'Heap Sort':
        heapSort(arr, drawRectangle, sort_speed.get())

#gui part


optionFrame = tk.Frame(root, width=900, height=300, bg='green')
optionFrame.grid(row = 0, column= 0, padx=10 , pady=10);

barWindow = tk.Canvas(root, width=750, height=550, bg='grey')
barWindow.grid(row=1, column=0, padx=10, pady=5);

tk.Label(optionFrame, text="Algorithms options" ,).grid(row=0, column=0, padx=10, pady=10)


algorithmMenu = ttk.Combobox(optionFrame, textvariable=select_algorithm, width=10);
algorithmMenu['values'] = ('Bubble Sort', 'Merge Sort', 'Heap Sort', 'Quick Sort', 'Selection Sort')
algorithmMenu.grid(row=0, column=1, padx=5, pady=5)
algorithmMenu.current(0);


sort_speed = Scale(optionFrame, from_=0.1, to=2.0, length=180, digits=2, resolution=0.2, orient=HORIZONTAL, label='Sorting Speed');
sort_speed.grid(row=0, column=2, padx=10, pady=10);



Button(optionFrame, text="Start Sorting", command=sorting, bg='red',height=5).grid(row=0, column=3, padx=5, pady=5)

lowest_entry = Scale(optionFrame, from_=0, to=100, length=250, digits=1, resolution=0.2 , orient=HORIZONTAL , label='Lowest Entry');
lowest_entry.grid(row=1, column=0, padx=10, pady=10);


highest_entry = Scale(optionFrame, from_=100, to=10000, length=250, digits=1, orient=HORIZONTAL, label="Highest Entry");
highest_entry.grid(row=1, column=1, padx=10, pady=10);

size_entry = Scale(optionFrame, from_=10, to=100, length=180, digits = 1, orient=HORIZONTAL, label="Array Size");
size_entry.grid(row=1, column=2, padx=10, pady=10)




Button(optionFrame, text="Current Array", command=genrate_array, bg='blue',height=5).grid(row=1, column=3, padx=10, pady=10)

# yha s code useless mann kr chlo

import time;
from random import randint
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


# algos 
from Algorithms.quickSort import quickSort_Complex
from Algorithms.bubbleSort import bubble_sort_Complex
from Algorithms.heap_sort import heapSort_Complex
from Algorithms.merge_sort import mergeSort_Complex
# from Algorithms.insertion_sort import
from Algorithms.selection_sort import selection_sort_Complex

def plot():
        
    list1 = [randint(0,2000) for i in range(1000)]
    times = [];

    for x in range(0,2001,100):
        start_time = time.time()

        if(select_algorithm.get() == "Bubble Sort"):
            list2 = bubble_sort_Complex(list1[:x]);

        elif(select_algorithm.get() == "Quick Sort"):
            list2 = quickSort_Complex(list1[:x])
        
        elif select_algorithm.get() == "Heap Sort":
            list2 = heapSort_Complex(list1[:x]);
       
        elif select_algorithm.get() == "Selection Sort":
            list2 = selection_sort_Complex(list1[:x]);
       
        elif select_algorithm.get() == "Merge Sort":
            list2 = mergeSort_Complex(list1[:x]);


        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

    # print(times);
    x=[i for i in range(0,2001,100)]

    figure1 = plt.Figure(figsize=(6,5), dpi=100)
    # plt.xlabel("No. of elements")
    # plt.ylabel("Time required")
    plot1 = figure1.add_subplot(111)
    plot1.plot(x, times);


    
    canvas = FigureCanvasTkAgg(figure1,master = barWindow)  
    canvas.draw()
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,barWindow)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
    bar1 = FigureCanvasTkAgg(figure1, root)





# def openNewWindow():
#     newWindow = Toplevel(root);
#     newWindow.title("Complexity Of "+select_algorithm.get());
#     newWindow.geometry("400x400")
#     plt_btn = Button(newWindow, text="Draw Graph", command= plot)
#     plt_btn.pack();


btn = Button(optionFrame,text ="Complexity", command = plot, height=5, bg='white')
btn.grid(row = 0, column=4, padx=5, pady=5)
    
    # Label(newWindow, text ="This is a new window").pack()




root.mainloop();