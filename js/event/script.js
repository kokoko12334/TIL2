"use strict";

const myButton = document.querySelector("#myButton");
console.log(myButton.textContent);

// 클릭 이벤트
myButton.addEventListener('click', function() {
    console.log("clickccc", this);
});



// 마우스 갇다댐 함수를 상수처럼 지정해서 관리 가능 이때 이 문법의 방식은 this가 상위 스코프(주로 window)로 바인딩
const logEnter = () => {console.log("const enter", this)};
const logLeave = () => {console.log("const levave")};

myButton.addEventListener('mouseenter', logEnter);
myButton.addEventListener('mouseleave', logLeave);


// 이벤트 객체 e를 통해 조작 가능 이때 여러개 이벤트리스너를 등록가능
const $click = document.querySelector("#clickPosition");
$click.addEventListener("click", function(e) {
    console.log(e);
    $click.textContent = "ddd";
});

$click.addEventListener("click", function(e) {
    console.log(e);
    $click.textContent = "asdads";
});


// input 관련
const $input = document.querySelector('#myInput');

$input.addEventListener('focus', () => {
    $input.setAttribute('placeholder', "focusonyou");
})

$input.addEventListener('blur', () => {
    $input.setAttribute('placeholder', "bluronyou");
})

// 값이 변경되고 딴곳 클릭 or enter
$input.addEventListener('change', (e) => {
    console.log("end", e.target.value);
})


// 키보드에 값이 입력되는 경우 화살표에 INSERT나 거의 모든것
$input.addEventListener('keyup', (e) => {
    console.log(e.key);
})