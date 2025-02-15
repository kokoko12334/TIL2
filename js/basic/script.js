"use strict"; // user strict는 암묵적 전역 변수가 허용되지 않는것으로 함.





// window 객체
// window는 브라우저 환경에서의 전역 객체 브라우저의 최상위 객체

var var1 = 1; // var 키워드는 안써도 됨
// var2 = 2;
console.log(var1);
console.log(window.var1); // window.으로 조회가능


// 단, const, let으로 정의 된것을 블록 단위로 window에서 조회안됨.
const PI = 3.14;
let darkModeOn = true;

{
    let let1 = false;
    console.log(window.let1);
}
console.log(window.PI); // undefined
console.log(window.darkModeOn); // undefined
