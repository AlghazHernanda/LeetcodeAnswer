// https://leetcode.com/problems/word-break/
// https://github.com/cheatsheet1999/FrontEndCollection/blob/main/JS-Algo/Word%20Break.md

/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    let word = new Set(wordDict);
    let length = new Set(wordDict.map((word) => word.length));
    let start = new Set([0]);
    for (let i of start) {
        for (let j of length) {
            if (word.has(s.slice(i, i + j))) {
                start.add(i + j);
            }
        }
    }
    return start.has(s.length)
};