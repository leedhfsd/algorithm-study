function solution(board, moves) {
    let answer = 0;
    let goal = [];
    for (let i = 0; i < moves.length; i++) {
        let pick = moves[i] - 1;
        for (let j = 0; j < board.length; j++) {
            if (board[j][pick] === 0) continue;
            else if (board[j][pick] !== 0) {
                goal.push(board[j][pick]);
                board[j][pick] = 0;
                break;
            }
        }
        let len = goal.length;
        if (len >= 2) {
            if (goal[len-2] === goal[len-1]) {
                goal.pop();
                goal.pop();
                answer += 2;
            }
        }
    }
    return answer;
}
