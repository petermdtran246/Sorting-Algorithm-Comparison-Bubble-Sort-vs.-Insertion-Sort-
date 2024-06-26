import random
from datetime import datetime

def list_of_random_numbers(size):
    """
    Generate the list of random numbers

    Args:
    ----------------------------
        size(int): The number of random integers to generate

    Returns:
    ----------------------------
        list: A list containing random integers between 1 and 100000
    """
    random_list = []
    for _ in range(size):
        random_number = random.randint(1, 100000) # Generate a random integer
        random_list.append(random_number) # Add random number to the list
    return random_list

# Bubble Sort
def bubble_sort(arr):
    """
    Sorts a list using Bubble Sort algorithm.

    Args:
    -----------------------------------------
        arr(list): The list of numbers to be sorted

    Returns:
    -----------------------------------------
        list: The sorted list
    """
    n = len(arr)
    for i in range(n-1):
        for j in range(n- i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Insertion Sort
def insertion_sort(arr):
    """
    Sorts a list using Insertion Sort algorithm.

    Args:
    --------------------------------------------
        arr(list): The list to be stored

    Returns:
    --------------------------------------------
        list: the sorted list
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    # Generate random list
    data_size = 20000
    random_list = list_of_random_numbers(data_size)

    # Start time for Bubble Sort
    start_time_bubble = datetime.timestamp(datetime.now()) * 1000 # timestamp in milliseconds
    # Sort using Bubble Sort
    sorted_list_bubble = bubble_sort(random_list.copy())
    # End time for Bubble Sort
    end_time_bubble = datetime.timestamp(datetime.now()) * 1000 # timestamp in milliseconds
    # Calculate time taken for Bubble Sort
    bubble_sort_duration = end_time_bubble - start_time_bubble

    # Start time for Insertion Sort
    start_time_insertion = datetime.timestamp(datetime.now()) * 1000 # timestamp in milliseconds
    # Sort using Insertion Sort
    sorted_list_insertion = insertion_sort(random_list.copy())
    # End time for Insertion Sort
    end_time_insertion = datetime.timestamp(datetime.now()) * 1000 # timestamp in milliseconds
    # Calculate time taken for Insertion Sort
    insertion_sort_duration = end_time_insertion - start_time_insertion

    # Print results
    print(f'Bubble Sort took {bubble_sort_duration:.2f} milliseconds to sort {data_size} elements.')
    print(f'Insertion Sort took {insertion_sort_duration:.2f} milliseconds to sort {data_size} elements.')













