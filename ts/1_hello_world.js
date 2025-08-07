

// var는 블록스코프 외부 o 함수크로프 x 재선언 가능
// let, const는 블록스코프 외부 x 함수 스코프 x 재선언 불가능


// for (i=0; i<10; i++) {
//     var a = 3;
//     console.log(a);
// }



// 호이스팅 변수가 최상단으로 이동되는 것처럼 실행이 되는거
console.log(name);
var name = '123';
console.log(name);