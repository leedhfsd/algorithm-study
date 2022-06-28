function solution(array, commands) {
    let answer = [];
    for (let i = 0; i < commands.length; i++) {
        let [start, end , idx] = commands[i];
        answer.push(array.slice(start-1, end).sort((a, b) => a - b)[idx-1]);    
    }
    return answer;
}
