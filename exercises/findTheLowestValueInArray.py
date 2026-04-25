def findLowestValue(array):
    minValue = array[0];
    for i in range(1, len(array)):
        if array[i] < minValue:
            minValue = array[i];
    
    return print('The minimun value of the array is ' + str(minValue));

findLowestValue([1,2,3,4,5,6,0]);