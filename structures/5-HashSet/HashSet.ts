/*
    Set implementation using Javascript (with Typescript on top)
*/

// Create a Set from an array
const lettersFirstWay = new Set(["a", "b", "c"]);

// Create an empty Set and add values
const lettersSecondWay = new Set();
lettersSecondWay.add("a");
lettersSecondWay.add("b");
lettersSecondWay.add("c");

// Create a Set and add variables
const lettersThirdWay = new Set();
const a = "a";
const b = "b";
const c = "c";
lettersThirdWay.add(a);
lettersThirdWay.add(b);
lettersThirdWay.add(c);


// Working with set methods
const mySet = new Set();
mySet.add(1); // Set(1) { 1 }
mySet.add(5); // Set(2) { 1, 5 }
mySet.add("some text"); // Set(3) { 1, 5, 'some text' }

console.log(mySet.has(1)); // true
console.log(mySet.size); // 3

mySet.delete(5); // removes 5 from the set
console.log(mySet.has(5)); // false
console.log(mySet.size); // 2

mySet.clear(); // removes all elements from the set
console.log(mySet.size); // 0


// Iterations
const mySetTwo = new Set(["a", "b", "c"]);
for (const item of mySet) {
   console.log(item); // a, b, c
}
mySet.forEach((value) => {
   console.log(value); // a, b, c
});