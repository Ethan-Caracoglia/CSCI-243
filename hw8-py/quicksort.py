"""
This module contains functions for implementing a quicksort algorithm
"""
import threading

def quicksort(list): # takes an array as a parameter
    """
    quickSort: List( A ) -> List( A )
        where A is 'totally ordered'
    """
    if list == []: # if the array is empty then just return an empty array
        return []
    else: # if the array is not empty, return the sorted list using recursion
        pivot = list[0] # Set the pivot of the list to be the first element
        (less, same, more) = partition(pivot, list) # partition the list by the pivot and put them 
        # into a tuple of lists
        return quicksort(less) + same + quicksort(more) # Recursively call each list in the less 
        # and more list. This will occur again and again until the less and more lists return 
        # nothing

def partition(pivot, list):
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    """
    (less, same, more) = ([], [], []) # Initialize the three lists as empty lists
    for e in list: # Run a for each loop through the list and sort the them by their relation to 
        # the pivot
        if e < pivot:
            less.append(e)
        elif e > pivot:
            more.append(e)
        else:
            same.append(e)
    return (less, same, more) # Return a tuple of the lists 

def quicksort_threading(list):
    """
    Sorts a list using quicksort through threading instead of recursion
    """
    # Empty list ends thread branching
    if list == []: 
        return []
    # Split the list
    else: 
        pivot = list[0]
        (less, same, more) = partition(pivot, list)
        t1 = threading.Thread(target=quicksort_threading, args=(less, shared_list))
        t2 = threading.Thread(target=quicksort_threading, args=(more, shared_list))
        
        # Begin the threads
        t1.start()
        t2.start()
        
        # End them-
        t1.join()
        t2.join()