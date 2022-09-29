function solution(n) {
    var answer = 0;
    let sqrt = Math.sqrt(n);
    
    // 제곱이 아닐 때 -1 return
    if (sqrt % 1 !== 0) {
        answer = -1;
    }
    else {
        answer = Math.pow(sqrt+1, 2);
    }
    
    return answer;
}