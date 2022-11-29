function solution(order) {
    var answer = 0;
    const num = order.toString()
    
    for (let i = 0; i < num.length; i++) {
        if (num[i] ==3 || num[i] == 6 || num[i] == 9) {
            answer += 1;
        }
    }
    
    return answer;
}