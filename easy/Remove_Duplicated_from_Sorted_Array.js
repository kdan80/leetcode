//  Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
//
// Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
//
// Return k after placing the final result in the first k slots of nums.
//
// Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

// Solution
//
// Loop throught the array
// Check if each value is equal to the next value in the array
// If it is equal remove it from the array and decrement the index
// If it is not equal move to the next value and repeat
// There is no need to return any value as we are modifying the num array in place
// e.g using a side effect

var removeDuplicates = function(nums) {
    for(let i = 0; i < nums.length; i++){
        if(nums[i] === nums[i+1]){
            nums.splice(i, 1);
            i--;
        }
    }
};

//nums = [0,0,1,1,1,2,2,2,3,3,3,4]
nums = [1,1,2]

removeDuplicates(nums);

console.log("new arr:", nums)
