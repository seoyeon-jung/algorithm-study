function solution(my_string, num1, num2) {
    // num1과 num2 숫자를 바꾸면 된다
    // splice: 배열의 기존 요소를 삭제 또는 교체하거나 새 요소를 추가하여 배열의 내용을 변경
    // 원본 배열을 수정하는 것
    // splice(start, deleteCount, item1)
    // start: 배열 변경 시작할 인덱스
    // deleteCount : 삭제할 요소의 수
    // item1 : 배열에 추가할 요소
    
    // => num1 위치에서 하나 삭제하고 num2를 넣어준다
    // num2도 마찬가지
    
    const result = [...my_string];
    
    result.splice(num1, 1, my_string[num2]);
    result.splice(num2, 1, my_string[num1]);
    
    return result.join("");
}