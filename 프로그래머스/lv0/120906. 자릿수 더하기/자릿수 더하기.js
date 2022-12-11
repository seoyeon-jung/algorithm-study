function solution(n) {
    var answer = 0;
    let num = String(n)
    
    for (let i = 0; i < num.length; i++) {
        answer += parseInt(num[i])
    }
    
    return answer;
}