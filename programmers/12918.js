function solution(s) {
    let answer = true;
    if (s.length === 4 || s.length === 6) {
        let num = ["0","1","2","3","4","5","6","7","8","9"];
        for (let i = 0; i < s.length; i++) {
            if (!num.includes(s[i])) {
                answer = false;
                break;
            }
        }
    } else 
        answer = false;
    return answer;
}
