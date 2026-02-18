const A = [23,34,[45,67],76,[12,[17],91],3];
A.push(1);
A.unshift(2);
//console.log(A);
A.pop();
//console.log(A);

const B = [23,34,87,12,5];
//const C = B.splice(1,4);
//console.log(C);
const X = [1,2,34];
const D = B.concat(X);
const E = [...B,...X];
//console.log(E);
const F = A.flat(2);
console.log(F);
//console.log(D);