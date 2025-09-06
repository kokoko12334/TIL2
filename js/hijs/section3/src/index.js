// const moduleData = require("./math");
// console.log(moduleData); //모듈이름, 함수가 나옴.

// console.log(moduleData.addition(1, 2));
// console.log(moduleData.sub(1, 2));


// //혹은 구조분해 할당 문법을 이용함 이때 키값 일치해야 함.
// const {addition, sub} = require("./math");

// console.log(addition(1, 2));
// console.log(sub(1, 2));

//ESM방식(확장자까지 적어야 함.)
import {add, sub} from "./math.js";
import { add2 } from "./math.js";
import s from "./math.js";
console.log(add(1, 2));
console.log(sub(1, 2));
console.log(add2(1, 2));
console.log(s(1, 2));

//라이브러리 실습1(라이브러리는 그냥 이름만 명시만 해도 됨.)
import randomColor  from "randomcolor";

const color = randomColor();
console.log(color);

