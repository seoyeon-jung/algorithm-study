function solution(s) {
    // 단어 => 숫자로
    // 숫자면 상관없음
    
    let numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
    
    for (let i = 0; i < numbers.length; i++) {
        let arr = s.split(numbers[i]);
        s = arr.join(i);
    }
    
    return Number(s);
}