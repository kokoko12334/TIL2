//1.배열 생성

let arrA = new Array();
let arrB = [];

let arrC = [1,2,"CCC",() => {},5];
console.log(arrC);

//2. 배열 조회

let item1 = arrC[3];
console.log(item1);


//3. 수정
arrC[0] = "hello";
console.log(arrC[0]);