// Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

// For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
//
// Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
//
//     I can be placed before V (5) and X (10) to make 4 and 9.
//     X can be placed before L (50) and C (100) to make 40 and 90.
//     C can be placed before D (500) and M (1000) to make 400 and 900.
//
// Given a roman numeral, convert it to an integer.



// Solution
// Check for subtractive numerals eg IV, IX first
// Add them to an integer and remove from the Roman numeral string
// All remaining numerals must be single values
// Iterate over them and add to the integer
// Return the integer

const dict = {
    "i": 1,
    "v": 5,
    "x": 10,
    "l": 50,
    "c": 100,
    "d": 500,
    "m": 1000
}

const subDict = {
    "iv": 4,
    "ix": 9,
    "xl": 40,
    "xc": 90,
    "cd": 400,
    "cm": 900
}

var romanToInt = function(s) {
    let int = 0;
    s = s.toLowerCase();

    // Check for subtractive numerals first and remove them
    for(const [key, value] of Object.entries(subDict)){
        for(let i = 0; i < s.length -1; i++){
            let x = [s[i], s[i+1]].join("").toString();
            if(x === key){
                int += value;
                s = s.replace(x, "");
            }
        }
    }

    for(const [key, value] of Object.entries(dict)){
        for(let i = 0; i < s.length; i++){
            if(s[i] === key){
                int += value;
            }
        }
    }

    console.log(int);
    return int;
};

s = "MCMXCIV"

romanToInt(s);
