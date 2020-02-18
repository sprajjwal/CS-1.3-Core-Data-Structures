#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found
    Best case: O(1); worst case: O(n)
    """
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    """
    Best case: O(1); worst case: O(n)
    """
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    """
    Best case: O(1); worst case: O(n)
    """
    # TODO: implement linear search recursively here
    if index == len(array):
        return None
    if array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index+1)
    
    
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found
    Best case: O(1); worst case: O(n)
    """
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item, 0, len(array)-1)


def binary_search_iterative(array, item):
    """
    Best case: O(1); worst case: O(n)
    """
    low = 0
    high = len(array) -1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] > item:
            high = mid - 1
        elif array[mid] < item:
            low = mid + 1
        elif array[mid] == item:
            return mid
    return None
    # implement binary search iteratively here
    # pass
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    """
    Best case: O(1); worst case: O(n)
    """
    if left > right:
        return None
    mid = (left + right) // 2
    if array[mid] > item:
        return binary_search_recursive(array, item, left, mid-1)
    elif array[mid] < item:
        return binary_search_recursive(array, item, mid+1, right)
    elif array[mid] == item:
        return mid
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

if __name__ == "__main__":
    array = [2, 3, 5, 7, 23]
    # print(linear_search(array, 7))
    print(binary_search(array, 22))