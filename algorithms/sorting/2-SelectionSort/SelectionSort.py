"""
    FOR EVERY ITERATION, TAKE THE LOWEST VALUE AND SWAP IT WITH THE INDEX OF THE LOOP

    This algorithm sorts an array by split the array in two: the ordered and unordered array
    We look for the lowest value in the unordered array and pass it to the ordered array
"""

arrayToSort = [1,3,5,4,9,6,7];

def selectionSort(array: list[int]):
    n = len(array)
    
    for i in range(n - 1):
        minValue = i
        for j in range (i + 1, n): 
            if (array[j] < array[minValue]):
                minValue = j
        array[i] = array[minValue]
        
    return array

print(selectionSort(arrayToSort))