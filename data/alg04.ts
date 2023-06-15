/**
 * Test file
 *
 * This file contains examples covering most tokens
 */

// Import
import { exampleFunction } from './exampleModule';

// Variables and data types
let a: number = 5;
const b: boolean = true;
let str: string = "Hello, world!";

// Control structures
if (a < 10) {
    console.log("a is less than 10");
} else {
    console.log("a is greater than or equal to 10");
}

for (let i = 0; i < 5; i++) {
    console.log("Iteration: " + i);
}

while (a > 0) {
    console.log("a is " + a);
    a--;
}

// Functions
function sum(x: number, y: number): number {
    return x + y;
}