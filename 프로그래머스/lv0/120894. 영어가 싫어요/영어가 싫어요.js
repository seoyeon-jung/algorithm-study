function solution(numbers) {
    const numsN = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    
    numsN.forEach((str, index) => {
        numbers = numbers.split(str).join(index)
    })
    
    return Number(numbers)
}