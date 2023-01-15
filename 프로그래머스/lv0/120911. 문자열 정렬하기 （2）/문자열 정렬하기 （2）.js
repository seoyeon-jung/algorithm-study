  // 1. 소문자로 바꾸기
    // 2. 알파벳 순서대로 정렬

const solution = (my_string) => my_string.split("").map(str => str.toLowerCase()).sort().join("")

