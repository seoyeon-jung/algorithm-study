function solution(num_list, n) {
    const result = [];
    
    for (let i = 0; i < num_list.length;) {
        const arrN = [];
        for (let j = 0; j < n; j++) {
            arrN.push(num_list[i])
            i++;
        }
        result.push(arrN)
    }
    return result;
}