"use strict";

// documnet객체(dom 조작): document는 현재 브라우저에서 로드된 웹페이지(HTML 문서)를 표현하는 객체입니다

// tag
const $lis = document.getElementsByTagName("li");
console.log($lis);

//classname
const $plant = document.getElementsByClassName("plant");
console.log($plant);

//id
const $sweets = document.getElementById('sweets');
console.log($sweets);


//css 
console.log(document.querySelector('section'));
console.log(document.querySelectorAll('section'));

console.log(document.querySelector('section#sweets')); // #는 id
console.log(document.querySelector('section.plant')); // .는 class

console.log(document.querySelector(".plant > ul > li")); // > 자식태그 조회
document.querySelector('section ul li');

console.log(document.querySelector("section").children); // 자식태그들 모두 조회
console.log(document.querySelector("section").firstElementChild); // 자식태그 첫번째
console.log(document.querySelector("section").lastElementChild); // 자식태그 마지막
console.log(document.querySelector("section").parentElement); // 부모섹션

//html 조작

const $carrot = document.querySelector('section ul li');
console.log($carrot.classList);
console.log($carrot.textContent);

$carrot.textContent = "carrot"

// 배열로 처리됨
const $onion = document.querySelector("section ul").lastElementChild; // 마지막요소로 접근하면 배열로 처리
console.log($onion.classList);

$onion.classList.add("on"); // class 추가
$onion.classList.remove("soldout");
$onion.classList.toggle("soldout"); //추가 제거
console.log($onion.classList);

// css 속성
$onion.style.fontSize = '20px'; //-는 대문자로 대체

// a태크
const $link = document.querySelector("a");

console.log($link.getAttribute("href"));
$link.setAttribute("href", "https://www.google.com");


