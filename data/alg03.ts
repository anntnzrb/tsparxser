/**
 * A minimal TypeScript Factorial function example
 *
 * This script calculates the factorial of a given number using an iterative
 * approach.
 *
 * Author: Christopher Villa
 */

function factorialize(num: number): number {
  if (num === 0 || num === 1) {
    return 1;
  }
  for (let i = num - 1; i >= 1; i--) {
    num *= i;
  }
  return num;
}

console.log(factorialize(5));