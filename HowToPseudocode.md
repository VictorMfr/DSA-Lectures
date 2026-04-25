# How to pseudocode

It's not a strict rule, but it comes handy if you're designing a solution. Pseudocode means write something that looks like code but it's human friendly to read. Therefore, it's not following a specific syntax (people might invent some, though). 

It might look like a recipe, for example, when finding the lowest value in an array:

- Create a variable 'minVal' and set it equal to the first value of the array.
- Go through every element in the array.
- If the current element has a lower value than 'minVal', update 'minVal' to this value.
- After looking at all the elements in the array, the 'minVal' variable now contains the lowest value.

Or it might look like code:

```
Variable 'minVal' = array[0]
For each element in the array
    If current element < minVal
        minVal = current element
```

(Examples taken from w3schools)