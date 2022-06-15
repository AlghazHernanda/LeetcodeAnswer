// https://leetcode.com/problems/two-sum/
// cara jalanin: node namafile.js

// Given an array of integers nums and an integer target, return indices of the two numbers 
// such that they add up to target.

// You may assume that each input would have exactly one solution, 
// and you may not use the same element twice.

// You can return the answer in any order.

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {

    //tambahan
    console.log(nums);
    console.log(target);
    console.log("");

    //core
    for (let index = 0; index < nums.length; index++) {
        console.log("index = " + index); //tambahan

        const diff = target - nums[index];
        console.log("target=" + target + " - nums=" + nums[index] + " = " + diff); //tambahan

        const diffIndex = nums.indexOf(diff);
        console.log("nums.indexOf(diff) = " + diffIndex); //tambahan
        console.log(""); //tambahan

        // "diffIndex !== index" takes care of same index not being reused
        console.log("jika " + diffIndex + " !== -1 && " + diffIndex + " !== " + index); //tambahan
        console.log(""); //tambahan

        if (diffIndex !== -1 && diffIndex !== index) {
            return [index, diffIndex];

        }
    }
}

//tambahan
//[2, 7, 11, 15]
//6
nums = [3, 2, 4];
target = 6;
console.log(twoSum(nums, target))