function solution(age) {
    // 알파벳이랑 나이 하나씩 매칭
    let alphabet = {
        0: 'a',
        1: 'b',
        2: 'c',
        3: 'd',
        4: 'e',
        5: 'f',
        6: 'g',
        7: 'h',
        8: 'i',
        9: 'j'
    };
    
    let result = age + "";
    
    return result.split("").map((n) => alphabet[n]).join("")
    
}