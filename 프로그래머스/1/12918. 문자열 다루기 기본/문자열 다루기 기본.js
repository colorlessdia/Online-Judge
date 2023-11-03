function solution(s) {
  if (s.length === 4 || s.length === 6) {
    for (let c of s) {
      if (!(0 <= parseInt(c) && parseInt(c) <= 9)) {
          return false;
      }
    }
    return true;
  } else {
    return false;
  }
}