# Hash Set

Hash Set is a type of data structure that use a "hash function" to generate "hash codes" which are a "unique" index for every value to be inserted in the set. 
    
### How it works:
- You want to store a number
- That number must be passed to the hash function
- The function returns a Hash Code
- Store the value with index = Hash Code

Think of it as an array, You must create a function that always generate a unique hash code. But in some cases you can't avoid them, and some hashcodes are equal, making them to "collide". Because that may happen, values are stored in buckets (often implemented as linked lists) inside of the bigger array and stored as the element, so you have a structure like this: [[],[],[],[]]

Almost every programming language has built their own hash function algorithms, so you don't have to create one from scratch

## What is it used for?

- To rapidly check if a value is in the set with almost $O(1)$ time complexity