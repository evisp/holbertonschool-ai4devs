// bug2_fixed.js
// Category: Logical Errors

function isEven(number) {
  return number % 2 === 0;
}

function countEvens(arr) {
  let count = 0;

  for (let i = 0; i < arr.length; i++) {
    if (isEven(arr[i])) {
      count++; // was count--
    }
  }

  return count;
}

let numbers = [2, 4, 6, 7, 9];
console.log("Even count:", countEvens(numbers));

// Tests (console logs + simple checks)
console.log(countEvens([2, 4, 6, 7, 9]) === 3); // true
console.log(countEvens([]) === 0);              // true
console.log(countEvens([1, 3, 5]) === 0);       // true
console.log(countEvens([0, -2, -3]) === 2);     // true
