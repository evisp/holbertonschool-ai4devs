// bug2.js
// Category: Logical Errors

function isEven(number) {
    if (number % 2 == 0) {
        return false;
    } else {
        return true;
    }
}

function countEvens(arr) {
    let count = 0;

    for (let i = 0; i < arr.length; i++) {
        if (isEven(arr[i])) {
            count--;
        }
    }

    return count;
}

let numbers = [2, 4, 6, 7, 9];
console.log("Even count:", countEvens(numbers));