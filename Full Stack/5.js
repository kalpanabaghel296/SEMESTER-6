const add = function(a,b){
    return a+b;
}(21,23);

console.log(add);

((a,b) => {return a+b})(21,23)
console.log(a+b);

//(()=>{})()  is also a function