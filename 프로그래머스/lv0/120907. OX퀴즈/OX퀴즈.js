function solution(quiz) {
    let answer = [];
    
    quiz.forEach((num) => {
        let question = num.split(" ");
        
        const X = Number(question[0])
        const Y = Number(question[2])
        
        let calc = 0;
        
        if (question[1] === "+") {
            calc = X + Y;
        }
        else if(question[1] === "-") {
            calc = X - Y;
        }
        
        const result = Number(question[4])
        
        if (calc === result) {
            answer.push('O')
        }
        else if (calc !== result) {
            answer.push('X')
        }
    })
    
    return answer;
}