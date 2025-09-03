// 1. 변수(let): 재선언 불가능, 재할당 가능

let age = 27;
console.log(age);

// let age = 30;

age = 30;
console.log(age);


// 2. 변수(var): 재선언 가능, 재할당 가능

var name = "kmp";
console.log(name);

var name = "kmp2";
console.log(name);

name = "kmp3";
console.log(name);

// 2. 상수(const): 재선언 불가능, 재할당 불가능
const birth = "1997.01.07";
console.log(birth);



//var, let차이

//1. 재선언 가능여부

//2. 호이스팅(둘다 호이스팅이 되지만 var만 초기화됨.)

console.log(var1); // undefined
var var1 = 10;

// console.log(let1); //ReferenceError
// let let1 = 10;

//3. 스코프 차이

// var는 스코프가 함수외부냐 내부냐로 정함 즉 if, for문 등이 아님
if (true) {
    var a = 1;
}
console.log(a);

function foo() {
    var b = 1;
}
console.log(typeof b);


//let은 스코프기준선이 무조건 블럭단위

if (true) {
    let c = 1;
}
// console.log(c); // error남


//4. 전역과의 관계: var는 window의 프로퍼티가 되지만 let은 아님
var gv = "gv";
let gl = "gl";

console.log(window.gv);
console.log(window.gl);