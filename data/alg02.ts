/**
 * A minimal TypeScript Fibonacci function example
 *
 * This script calculates the nth Fibonacci number using an iterative approach.
 *
 * Author: Paul Gudiño
 */

function fibonacci(n: number): number {
    if (n < 1) {
        return 0;
    }
    let a = 0;
    let b = 1;
    for (let i = 1; i < n; ++i) {
        const c = a + b;
        a = b;
        b = c;
    }
    return b;
}

console.log(fibonacci(10)); 
