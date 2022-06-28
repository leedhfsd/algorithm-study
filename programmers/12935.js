//splice는 원본 배열을 변경한다. 
//splice(변경시작인덱스, 삭제할개수, ... 추가할 값들)
function solution(arr) {
    arr.splice(arr.indexOf(Math.min(...arr)),1);
    if(arr.length<1)
      return [-1];
    return arr;
}
