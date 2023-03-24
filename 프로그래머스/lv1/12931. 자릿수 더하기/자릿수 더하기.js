function solution(n)
{
    let answer = 0;
    let n_string = String(n);
    
   for (let i = 0; i < n_string.length; i++) {
        answer += parseInt(n_string[i])
    }
    
    return answer;
}