var twoSum = function(nums, target) {
    let arr = [];
    let n, o;

    for(let i = 0; i < nums.length; i++){
        n = i + 1;

        for(let j = n; j <= nums.length; j++){
            if(nums[i] + nums[j] === target) return arr = [i,j];
        }
    }
    return arr;
};

const nums = [1,4,12,16,5];
const target = 21;

const x = twoSum(nums,target)

console.log(x);
