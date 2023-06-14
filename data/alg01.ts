/**
 * A minimal TypeScript for loop example
 *
 * This script demonstrates a for loop by printing iteration number,
 * its square, and checking if it's even or odd.
 * 
 * Author: Juan Antonio
 */

for (let i: number = 0; i < 5; i++) {
    console.log("Iteration: " + i);

    let square: number = i * i;
    console.log("Square of " + i + " is: " + square);

    if (i % 2 === 0) {
        console.log(i + " is even");
    } else {
        console.log(i + " is odd");
    }
}