// Find the longest common prefix in an array of strings (if it exists)

// Solution
// Sort the array in ascending order of length
// The shortest element is the longest possible prefix should it exist
// Loop through the strs array and check if the remaing strings contain the chars of the shortest string
// If they do push the matching chars to the returned value

var longestCommonPrefix = function(strs) {
    let res = "";

    // If the strs is empty immediately return
    if(!strs.length) return res;

    // Sort strs in ascending order of length
    strs.sort((a,b) => a.length - b.length);

    // Extract the shortest string
    const str = strs[0];

    // Loop through the shortest string and check if each char is present in the remaining strings. If it is add the char to the result if it is not immediately return
    for(let i = 0; i < str.length; i++){
        for(let j = 1; j < strs.length; j++){
            if(str[i] !== strs[j][i]) return res;

        }
        res += str[i]
    }
    return res;
}

strs = ["flower","flow","flight"];

const prefix = longestCommonPrefix(strs);
console.log(prefix);
