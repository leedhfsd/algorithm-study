function solution(s) {
  let answer = s.replace(/zero/gi,"0")
                .replace(/one/gi,"1")
                .replace(/two/gi,"2")
                .replace(/three/gi,"3")
                .replace(/four/gi,"4")
                .replace(/five/gi,"5")
                .replace(/six/gi,"6")
                .replace(/seven/gi,"7")
                .replace(/eight/gi,"8")
                .replace(/nine/gi,"9");
  
  return parseInt(answer);
}


// split join 이용하는 깔끔한 방법
function solution(s) {
  let answer = s;
  let arr = ["zero","one","two","three","four","five","six","seven","eight","nine"];
  for (let i = 0 ; i < arr.length; i++) {
      answer = answer.split(arr[i]).join(i)
  }
  return Number(answer);
}
