// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
//
// An input string is valid if:
//
//     Open brackets must be closed by the same type of brackets.
//     Open brackets must be closed in the correct order.
//

// Solution
//
// Loop through string
// If a char is a propety of bracketDict and it complements the last element of the stack then we having a matching pair so we can pop it from the stack
// If it does not match but the stack is not empty we have an invalid string
// If it does match and the stack is empty then we should push it to the stack until we find the matching pair
// If after parsing the entire string the stack is not empty then we have an unclosed bracket which means an invalid string

var isValid = function(s) {

    stack = [];
    bracketDict = {
        ")":"(",
        "]":"[",
        "}":"{"
    }

    for(let i = 0; i < s.length; i++){
        if(s[i] in bracketDict){
            if(stack && stack[stack.length - 1] === bracketDict[s[i]]){
                stack.pop()
            }
            else {
                return false
            }
        }
        else {
            stack.push(s[i])
        }
    }

    return stack.length ? false : true;
};

let s = "()"
let sIsValid = isValid(s);
console.log(`"${s}" is valid = ${sIsValid}`);

t = "()[]{}";
const tIsValid = isValid(t);
console.log(`"${t}" is valid = ${tIsValid}`);

u = "(]";
const uIsValid = isValid(u);
console.log(`"${u}" is valid = ${uIsValid}`);
