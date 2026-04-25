# Bubble sort

Sorts an array from lower to higher values (not necessarily), making higher values to "bubble up". It has a Time complexity of O($n^2$), because

Procedure (w3schools):

- Go through the array, one value at a time.
- For each value, compare the value with the next value.
- If the value is higher than the next one, swap the values so that the highest value comes last.
- Go through the array as many times as there are values in the array.

Notes:

- If you can know how many times a loop might run, don't use while true loops, use for loops, it's safer
  - Really undefined repetition = while loops
  - Defined repetitions = for loops

```python
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
```