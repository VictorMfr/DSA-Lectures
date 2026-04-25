def findValue(array, value):
        for i in array:
            if (array[i] == value):
                return print('founded, it is at index ' + str(i))
        
        return print('not found');
    
    
arr = [1,2,3,4];
value = 3;

findValue(arr, value);