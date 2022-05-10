// 신고 결과 받기 https://programmers.co.kr/learn/courses/30/lessons/92334
function solution(id_list, report, k) {
  const answer = [];
  let reportList = {};
  let reportCount = {};
  id_list.map((v) => reportCount[v] = 0);
  id_list.map((v) => reportList[v] = []);
  report.map((v) => {
      const [a, b] = v.split(' ');
      if (!reportList[a]) {
          reportList[a] = [b];
      } else {
          if (!reportList[a].includes(b)){
              reportList[a].push(b);
          }
      }
  });
  for (let i = 0; i < id_list.length; i++) {
      if (reportList[id_list[i]].length > 0) {
          reportList[id_list[i]].map((v) => {
          reportCount[v]++;
          });
      }
  }
  for (let i = 0; i < id_list.length; i++) {
      let count = 0;
      reportList[id_list[i]].map((v) =>{
          if (reportCount[v] >= k) {
              count++;
          }
      });
      answer.push(count);
  }
  
  return answer;
}
