
function add(a, b) {
    return a + b;
}

function sub(a, b) {
    return a - b;
}

// //cjs: 키(외부에서 사용할 이름), value: 함수이름 이때 키, 밸류 값으면 굳이 키:밸류 안해도 됨.
// module.exports = {
//     addition: add,
//     sub,
// }


//ESM
export {add, sub};


// 함수자체에서 export 가능
export function add2(a, b) {
    return a + b;
}

//export default -> import 하는곳에서 중괄호 없이, 원하는 이름으로 지정가능
export default function sub2(a, b) {
    return a - b;
}