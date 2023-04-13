function solution(a, b, n) {
    // b < a <= n
    // n을 a로 나눈 최대값이 첫 번째 받는 콜라 병의 수
    // 다시 콜라병 수 구하기
    // 콜라병 수를 a로 나눈 최대값이 두번째 받는 콜라 병의 수
    
    let answer = 0;
    
    while (n >= a) {
        answer += Math.floor(n / a) * b
        n = Math.floor(n / a) * b + n % a
    }
    
    return answer;
}