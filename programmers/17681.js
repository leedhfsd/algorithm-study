function solution(n, arr1, arr2) {
    let answer = [];
    for (let i = 0; i < n; i++) {
        let map1 = arr1[i].toString(2);
        let map2 = arr2[i].toString(2);
        if (map1.length < n || map2.length < n) {
            map1 = "0".repeat(n-map1.length) + map1;
            map2 = "0".repeat(n-map2.length) + map2;
        }
        let temp = [];
        for (let j = 0; j < n; j++) {
            if (parseInt(map1[j]) + parseInt(map2[j]) >= 1){
                temp.push("#");
            } else {
                temp.push(" ");
            }
        }
        answer.push(temp.join(''));
    }
    return answer;
}
