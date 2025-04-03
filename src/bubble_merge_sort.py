def bubble_merge_sort(arr):
    """
    Custom sorting algorithm that combines Bubble Sort and Merge Sort.
    
    The algorithm works in two stages:
    1. Partially sort the array using Bubble Sort to reduce inversions
    2. Completely sort the array using Merge Sort
    
    Args:
        arr (list): Input list of comparable elements
    
    Returns:
        list: Sorted list in ascending order
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains elements that cannot be compared
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Stage 1: Bubble Sort (reduce inversions)
    def bubble_pass(arr):
        """Perform a single pass of bubble sort"""
        n = len(arr)
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        return swapped
    
    # Perform initial bubble sort passes to reduce inversions
    work_arr = arr.copy()
    for _ in range(len(work_arr) // 2):
        bubble_pass(work_arr)
    
    # Stage 2: Merge Sort
    def merge(left, right):
        """Merge two sorted sublists"""
        result = []
        i, j = 0, 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def merge_sort(arr):
        """Recursive merge sort implementation"""
        # Base case
        if len(arr) <= 1:
            return arr
        
        # Divide
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        
        # Conquer (merge)
        return merge(left, right)
    
    # Final sorting stage
    return merge_sort(work_arr)