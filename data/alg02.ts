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
