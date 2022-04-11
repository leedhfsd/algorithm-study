//출처 https://blinders.tistory.com/83
//문자열 찾기 kmp 알고리즘
const kmp = function(origin, keyword) {
  let originDump = origin.split('');
  let keywordDump = keyword.split('');
  let oLength = origin.length;
  let kLength = keyword.length;
  
  let failure = Array.from({length: origin.length}, () => -1);
  
  //failure 배열 초기화
  for (let i = 1; i < kLength; i++) {
    let idx = failure[i-1] + 1;
    if (keywordDump[i] === keywordDump[idx]) {
      failure[i] = idx;
    } else {
      failure[i] = -1;
    }
  }

  //origin에서 keyword 찾기 시작
  let n = 0, m = 0;
  while (m < kLength && n < oLength) {
    if (originDump[n] === keywordDump[m]) {
      n++;
      m++;
    } else if (m === 0) {
      n++;
    } else {
      m = 1 + failure[m-1];
    }
  }
  return m === kLength ? n - kLength : -1
}
