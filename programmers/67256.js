function solution(numbers, hand) {
    let answer = '';
    const leftBtn = [1,4,7];
    const rightBtn = [3,6,9];
    const graph = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]];
    let [leftHand, rightHand] = ["*", "#"];
    let [lpos, rpos] = [[3,0], [3,2]];

    function bfs (a, b, target) {
        let queue = [];
        let visited = new Array(4);
        let dx = [-1,1,0,0];
        let dy = [0,0,-1,1];
        for (let i = 0; i < 4; i++) {
            visited[i] = new Array(3).fill(0);
        }
        queue.push([a, b, 0]);
        visited[a][b] = 1;
        while (queue.length > 0) {
            let [x, y, count] = queue.shift();
            for (let i = 0; i < 4; i++) {
                nx = x + dx[i];
                ny = y + dy[i];

                if (nx < 0 || nx >= 4 || ny < 0 || ny >= 3 || visited[nx][ny] === 1) continue;
                if (graph[nx][ny] === target) return count+1;
                if (graph[nx][ny] !== target) {
                    queue.push([nx, ny, count+1]);
                    visited[nx][ny] = 1;
                }
            }
        }
    } 

    for (let i = 0; i < numbers.length; i++) {
        if (leftBtn.includes(numbers[i]) || numbers[i] === leftHand) {
            leftHand = numbers[i];
            answer += "L";
            continue;
        }
        if (rightBtn.includes(numbers[i]) || numbers[i] === rightHand) {
            rightHand = numbers[i];
            answer += "R";
            continue;
        }

        for (let i = 0; i < 4; i++) {
            for (let j = 0; j < 3; j++) {
                if (graph[i][j] === leftHand) {
                    lpos = [i, j];
                }
                if (graph[i][j] === rightHand) {
                    rpos = [i, j];
                }
            }
        }

        let diff = bfs(lpos[0], lpos[1], numbers[i]) - bfs(rpos[0], rpos[1], numbers[i]);
        if (diff < 0) {
            leftHand = numbers[i];
            answer += "L";
        } else if (diff > 0){
            rightHand = numbers[i];
            answer += "R";
        } else {
            if (hand === "left") {
                leftHand = numbers[i];
                answer += "L";
            } else {
                rightHand = numbers[i];
                answer += "R";
            }
        }

    }
    return answer;
}
