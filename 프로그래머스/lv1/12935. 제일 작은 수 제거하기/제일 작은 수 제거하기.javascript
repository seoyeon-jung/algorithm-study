function solution(arr) {
    
    // 빈 배열인 경우 [-1] 리턴
    if (arr.length <= 1) return [-1];
    
    let i = 0;
    for (let j = 0; j < arr.length; j+= 1) {
        if (arr[i] > arr[j]) i = j;
    }
    
    arr.splice(i, 1);
    return arr;
}