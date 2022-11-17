function solution(my_string, letter) {
    var answer = '';
    answer = [...my_string].filter(a => a != letter).join("")
    return answer;
}