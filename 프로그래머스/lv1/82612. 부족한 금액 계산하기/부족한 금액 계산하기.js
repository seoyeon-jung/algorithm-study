function solution(price, money, count) {
    // count번 타면 모자른 금액을 return
    // price+price*N = 필요한 요금
    // 필요한 요금 - money = return값
    
    let total = 0;
    
    for (let i = 1; i <= count; i++) {
        total += price * i
    }
    
    return money > total ? 0 : total-money;
}