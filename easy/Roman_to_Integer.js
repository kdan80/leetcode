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
