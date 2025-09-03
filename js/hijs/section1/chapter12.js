
function funcA() {
    console.log("funcA");
}

let varA = funcA;
console.log(varA);
varA();

let varB = function () {
    console.log("funcB"); // 익명함수-> 주의점이 호이스팅이 안됨
}
varB();

let varC = () => {
    return 1;
}

console.log(varC());



let varD = (a, b) => {
    return a + b;
}

console.log(varD(1, 2));