// null 병합 연산자: null, undefined가 아닌 값을 찾아내는 연산자

let var1;
let var2 = null;
let var3 = 20;
let var4 = 30;

// null이 아닌 값을 찾아서 반환, 이때 처음인 값을 반환
let var5 = var3 ?? var1 ?? var2 ?? var4;
console.log(var5);

// typeof: 타입을 문자열로 반환함

let var7 = 1;
let t1 = typeof var7;
console.log(t1);

// 삼항 연산자
let inputValue = 2;
const result = inputValue < 10 ? "Yes" : "No";
console.log(result);
