# The Big O Notation

Also refered as the Time Complexity, this is just a notation that tells how efficient is your code. But to be more clever, it tells the number of operations an algorithm would take to solve the problem in the worst case scenario.

if you were building a function that finds a value in an array, you'd start searching at the start of the array, all the way to the end. You might not even find that value.

An algorithm like the one above, could be coded like this:

```python
    def findValue(array, value):
        for i in array:
            if (array[i] == value):
                return print('founded, it is at index ' + i)
        
        return print('not found');
```

So in the worst case scenario, supposing that you have:

```python
array = [1,2,3,4,5,6]
value = 6

findValue(array, value)
```

It's going to take 6 operations to find the value, because it's at the end of the array, so we say in terms of Big O notation, that this algorithm is O(6).

But, to be more general, people assume that you don't know the length of the array, so instead of 6, we get "n". Therefore we say O(n).

Sometimes you'll see algorithms that takes Time Complexities from O(n), O($n^2$) to O($n \times Log(n)$), O($n \times m$), and so on