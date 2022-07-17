//Given an integer x, return true if x is palindrome integer.

//An integer is a palindrome when it reads the same backward as forward.

//For example, 121 is a palindrome while 123 is not.


// Solution
//
// Convert the int to a string (x)
// Iterate through over x in reverse order and push to a new array
// Convert new array to a string (y)
// Compare x to y and return

var isPalindrome = function(x) {
    x = x.toString();
    let y = [];

    for(let i = x.length - 1; i >= 0; i--){
        y.push(x[i]);
    }
    y = y.join('');

    return x === y;
};

const x = isPalindrome(121);
console.log(`121 is a palindrome = ${x}`);

const y = isPalindrome(1122);
console.log(`1122 is a palindrome = ${y}`);

const z = isPalindrome(1221);
console.log(`1221 is a palindrome = ${z}`);
