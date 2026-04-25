def bubbleSort(array):
        n = len(array);

        # We know n repetitions
        for i in range(n - 1):

            # For every new repetition in i, j 
            # must have smaller ranges because
            # the last element is already ordered  
            for j in range (n - i - 1):
                if array[j] > array[j + 1]:
                    array[j + 1], array[j] = array[j], array[j + 1]

        print(array);
        
        
bubbleSort([2,6,33,7,43]);