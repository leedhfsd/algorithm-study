function solution(n) {
    let answer = '';
    function recursion (n) {
        if (n === 1) return answer = "수";
        if (n % 2 === 0)
            answer += recursion(n-1) + "박";
        else 
            answer += recursion(n-1) + "수";
        return answer;
    }
    recursion(n);
    return answer;
}
