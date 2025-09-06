// async: 어떤 함수를 비동기 함수로 만들어주는 키워드
// async를 붙이면 Promise를 반환하는 함수가 됨.

async function getData() {
    return {
        name: "고",
        id: "ddd"
    }
}

console.log(getData()); // Promise를 반환함

//await: async 내부에서만 사용 가능한 키워드, 
// 비동기 함수가 다 처리되기를 기다리는 역할, then의 결과처리랑 같음
// 동기코드처럼 작성 가능
async function printData() {
    const data = await getData();
    console.log(data);
}

printData();