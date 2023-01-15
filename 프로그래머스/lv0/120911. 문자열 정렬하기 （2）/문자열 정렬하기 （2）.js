function solution(my_string) {
    // 1. 소문자로 바꾸기
    // 2. 알파벳 순서대로 정렬
    return my_string.toLowerCase().split('').sort().join('');
}

