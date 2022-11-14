function solution(array) {
    var answer = 0;
    
    // 배열을 정렬하기
    array.sort(function(a, b) {
        return a - b;
    });
    
    // 절반으로 나누어서 중앙 계산하기
    answer = Math.floor(array.length / 2)

    return array[answer]
}