function solution(s) {
  let answer = s.split(' ');
  for (let i = 0; i < answer.length; i++) {
      let word = answer[i].split('');
      for (let j = 0; j < word.length; j++) {
          if (j % 2 === 0) 
              word[j] = word[j].toUpperCase();
          else 
              word[j] = word[j].toLowerCase();
      }
      answer[i] = word.join('');
  }    
  
  return answer.join(' ');
}
