// https://leetcode.com/problems/product-of-array-except-self/
// https://alkeshghorpade.me/post/leetcode-product-of-array-except-self

var productExceptSelf = function(nums) {
    var answer = [];
    let product = 1;

    for (let i = 0; i < nums.length; i++) {
        answer[i] = product;
        product *= nums[i];
    }

    product = 1;

    for (let i = nums.length - 1; i >= 0; i--) {
        answer[i] *= product;
        product *= nums[i];
    }

    return answer;
};