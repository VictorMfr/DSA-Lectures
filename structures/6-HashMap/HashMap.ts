/*
    I also wanted to attatch the typescript implementation for this,
    since this is the programming language I mostly use
*/

function isAnagram(s: string, t: string): boolean {
    // 1. length validation
    if (s.length !== t.length) {
        return false;
    }

    // We define the object for counting: keys are char, values are numbers
    const count: { [key: string]: number } = {};

    for (let i = 0; i < s.length; i++) {
        const charS = s[i];
        const charT = t[i];

        // Increment for s
        count[charS] = (count[charS] || 0) + 1;
        // Decrement for t
        count[charT] = (count[charT] || 0) - 1;
    }

    // 2. If there's a value distinct from 0, it's not an anagram
    for (const key in count) {
        if (count[key] !== 0) {
            return false;
        }
    }

    return true;
}

// Use example
console.log(isAnagram("racecar", "carrace")); // true
console.log(isAnagram("jar", "jam"));         // false

/*
    Javascript also has a default function for HashMaps
    called Map<any,any>() that comes with default methods for it like
    get, set, etc.
*/

function isAnagramMap(s: string, t: string): boolean {
    if (s.length !== t.length) return false;

    const freqMap = new Map<string, number>();

    for (let i = 0; i < s.length; i++) {
        // Logic for string 's'
        freqMap.set(s[i], (freqMap.get(s[i]) || 0) + 1);
        
        // Logic for string 't'
        freqMap.set(t[i], (freqMap.get(t[i]) || 0) - 1);
    }

    for (let count of freqMap.values()) {
        if (count !== 0) return false;
    }

    return true;
}