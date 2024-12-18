"""
    A python implementation of the homework 8
"""
import sys
import io
import time
import threading as td
import quicksort as qs

def main():
    """
        The main function of the module which is responsible for processing all sys args and 
        processing said data.
    """
    # Setting up C-like argument vector
    argc = len(sys.argv)
    argv = sys.argv
    print("System args = ", argv)
    
    # Throw an error if not enough arguments were entered
    if argc < 2:
        print("Run failed: Please enter the arguments in the proper format <./main.py [-p] integer_file>")
        return -1
    
    # Begin the file processing sequence
    file = None
    should_print = False
    
    # Process the files and return the list to be sorted
    # "-p" entered
    if argc == 3 and argv[1] == "-p":
        print("-p statement found")
        file = open(argv[2], "rt")
        should_print = True
    # "-p" not entered
    elif argc == 2:
        print("No -p statement")
        file = open(argv[1], "rt")
    
    # Read from the file to build the list
    line = file.readline()
    list = []
    
    while line != "":
        num = int(line) 
        list.append(num)
        line = file.readline()
    
    # Print list if "-p" was entered
    if should_print:
        print(list)
    
    sorted_list = qs.quicksort(list);
    
    print("Recursion sorted list: ", sorted_list)
    
    print("Now sorting using threads")
    
    sorted_thread_list = list
    qs.quicksort_threading(list)
    
    return 0

if __name__ == "__main__":
    main()