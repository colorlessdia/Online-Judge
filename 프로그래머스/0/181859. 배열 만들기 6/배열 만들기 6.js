function solution(arr) {
    let stk = [];
    
    for (let i = 0; i < arr.length; i++) {
        if (stk.length === 0) {
            stk.push(arr[i])
        } else if (0 < stk.length && stk[stk.length - 1] === arr[i]) {
            stk.pop()
        } else if (0 < stk.length && stk[stk.length - 1] !== arr[i]) {
            stk.push(arr[i])
        }
    }
    
    if (stk.length === 0) {
        return [-1]
    }
    
    return stk;
}