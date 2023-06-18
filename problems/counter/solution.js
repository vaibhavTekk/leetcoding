/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let count = n
    return function() {
        temp = count;
        count += 1
        return temp;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */