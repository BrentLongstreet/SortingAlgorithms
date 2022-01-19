"""
Name: Brent Longstreet
Date: 02/18/2020
Project: Sorting III
"""

import matplotlib.pyplot as plt
import random
import numpy as np
import copy
import time
import sys


sort_times = [] #Empty list for sort timers
names = ["Bubble Sort", "Selection Sort", "Insertion Sort"] #list of sort names
class Timer(object):
    #code for timer
    def __init__(self, verbose=False):
        self.verbose = verbose 

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print ('elapsed time: %f ms' % self.msecs)
            t = int(self.msecs)
            sort_times.append(t)
            
            
def bubbleSort(arr):
    #Code for bubblesort
    with Timer(True): #timer
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1] : 
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    

def selectionSort(arr):
    #Code for selection sort
    with Timer(True): #timer
        for i in range(len(arr)): 
            min_idx = i 
            for j in range(i+1, len(arr)): 
                if arr[min_idx] > arr[j]: 
                    min_idx = j          
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertionSort(arr):
    #Code for insertionsort
    with Timer(True): #timer
        for i in range(1, len(arr)): 
            key = arr[i] 
            j = i-1
            while j >= 0 and key < arr[j] : 
                    arr[j + 1] = arr[j] 
                    j -= 1
            arr[j + 1] = key


def plotDictionary(times, names, title):
    #BAR GRAPH
    N = len(names)
    ind = np.arange(N)
    width = .25
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, times, width, color='r')
    ax.set_ylabel('Time (ms)')
    ax.set_title("Sort Bar Graph")
    ax.set_xticks(ind + width)
    ax.set_xticklabels(names)
    plt.show()

def lineGraph(names, times):
    #LINE GRAPH
    N = len(names)
    ind = np.arange(N)
    plt.ylabel('Time (ms)')
    plt.title('Sort Line Graph')
    plt.plot(names, times)   
    plt.show()
    plt.close()

def Main():
    while(True):#Loop for sort
        num_list = input("Enter the number of lists to sort: ")
        num_numbers = input("Enter the amount of numbers per list: ")
        num_list = int(num_list)
        num_numbers = int(num_numbers)
        a = np.array([random.sample(range(10000), num_numbers) for x in range(num_list)])
        print('\n')
        result = a.flatten() #turning 2d array into 1d
        original = copy.deepcopy(result) #copying the 1d array
        print("Begin Sorting...")
        print('\n')
        bubbleSort(result)
        print("Bubble Sort Complete")
        print('\n')
        original2 = copy.deepcopy(original)
        selectionSort(original)
        print("Selection Sort Complete")
        print('\n')
        original3 = copy.deepcopy(original2)
        insertionSort(original2)
        print("Insertion Sort Complete")
        print('\n')
        while(True):
            graph_input = input("Enter 'B' for BAR GRAPH, 'L' for LINE GRAPH OR 'C' to continue: ").upper()
            if graph_input == "B":
                #BAR GRAPH
                plotDictionary(sort_times, names, "Sorting Graph")
                print('\n')
                continue
            elif graph_input == "L":
                #LINE GRAPH
                lineGraph(names, sort_times)
                print('\n')
                continue
            elif graph_input == "C":
                print('\n')
                break
            else:
                print("Invalid Input")
                continue
        while(True):
            loop_result = input("Enter 'Q' to quit or 'N' to enter a New List of Numbers: ").upper()
            if loop_result == "Q":
                sys.exit()
            if loop_result == "N":
                print('\n')
                sort_times.clear()
                break
            else:
                print("Invalid Input")
                continue
            
        

Main()

