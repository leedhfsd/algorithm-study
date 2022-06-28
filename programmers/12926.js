function solution(s, n) {
    let answer = "";
    let small = "a".charCodeAt();
    let big = "A".charCodeAt();
    
    for (let i = 0; i < s.length; i++) {
        if (s[i] === " ") {
            answer += " ";
            continue;
        }
        let ascii = s[i].charCodeAt();
        if (ascii <  small) {
            ascii = (ascii - big + n) % 26 + big;
            answer += String.fromCharCode(ascii);
        } else {
            ascii = (ascii - small + n) % 26 + small;
            answer += String.fromCharCode(ascii);
        }
        
    }
    return answer;
}
