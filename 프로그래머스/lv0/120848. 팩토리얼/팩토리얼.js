function solution(n) {
    // result! <= n
    // 2! 부터 계속 계산해서 n에 도달하는지 계산하기
    // n은 최대 10!까지만 계산할 수 있다
    
    let result = 0;
    
    // 팩토리얼 함수에 i를 넣으면서 n과 같거나 작으면 result = i
    for(let i = 1; i <= 10; i++) {
        if (n >= getFac(i)) {
            result = i
            continue
        }
        else {
            break;
        }
    }
    
    return result;
}

// 팩토리얼 구하는 함수 (재귀 이용)
function getFac(num) {
    if (num > 1)
        return num * getFac(num-1);
    
    return num;
}