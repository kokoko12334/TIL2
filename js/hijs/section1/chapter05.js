//원시타입: Number, String, Boolean, Null, Undefined


//1. Number
let num1 = 27;
let num2 = 1.5;
let num3 = -20;

console.log(num1 + num2);
console.log(num1 * num2);
console.log(num1 % num2);
console.log(num1 / num2);
console.log(num1 - num2);

let inf = Infinity;
let mInf = Infinity;
let nan = NaN; // 연산에 실패함

console.log(1 *"hhh"); // Not a Number

//2. String
let myName = "김정환";
let myLocation = "서울";
let introduce = myName + myLocation;
console.log(introduce);

let introducetext = `이름: ${myName}, 주소:${myLocation}`;
console.log(introducetext);

//3. Boolean

let isSwitchOn = true;
let isEmpty = false;

//4. Null(암것도 없다)
let empty = null;

//5. Undefined(선언만 하고 암것도 할당 안할때 자동으로 초기화)
let none;
console.log(none);


//객체 타입: Object -> Array, Function, RegexExp












