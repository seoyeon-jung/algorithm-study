function solution(array, n) {
    let new_arr = []
    for(let i = 0; i < array.length; i++) {
        if (array[i] === n) {
            new_arr.push(array[i])
        }
    }
    return new_arr.length;
}