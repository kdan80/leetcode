//Given an array of integers, nums, and an integer, target, return indices of the two numbers such that they add up to target.

//You may assume that each input would have exactly one solution, and you may not use the same element twice.

//You can return the answer in any order.


// Solution
//
// For each element in the nums array we need to add it to the remaining elements, in turn, and check if those values are equal to the target
// We do not need to check against earlier elements in the array

var twoSum = function(nums, target) {
    let arr = [];
    let n, o;

    for(let i = 0; i < nums.length; i++){
        for(let j = i + 1; j <= nums.length; j++){
            if(nums[i] + nums[j] === target) return arr = [i,j];
        }
    }
    return arr;
};

const nums = [1,4,12,16,5];
const target = 21;

const arr = twoSum(nums,target)

console.log(arr);
