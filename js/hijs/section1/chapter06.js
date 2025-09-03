// 1.묵시적 형변환(js엔진이 알아서 형변환함)

let num = 10;
let str = "20";

const result = num + str;
console.log(result); //Number, String연산 시에 Number -> String변환

//2. 명시적 형변환
let str1 = "10";
let strToNum1 = Number(str1);
console.log(10 + strToNum1);

let str2 = "20개개개";
let strToNum2 = Number(str2);
let strToNum3 = parseInt(str2);
console.log(strToNum2); // NaN
console.log(strToNum3); // 20으로 알아서 숫자만 걸려줌 단, 숫자가 맨 앞에 있어야 함.



let num1 = 20;
let numberToStr1 = String(num1);
console.log(typeof numberToStr1);




