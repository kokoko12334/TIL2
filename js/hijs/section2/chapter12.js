// Promise: 비동기 관련 작업을 관리하는 객체

/* 

1. Pending: 대기(아직 작업이 진행중) 
2. Fulfilled: 성공(작업이 성공적으로 완료됨) 
3. Rejected: 거부(작업이 실패함)

*/

const promise = new Promise((resolve, reject) => {
    //비동기 작업 수행
    setTimeout(() => {

        const num = 20;
        if (typeof num === "number") {
            resolve(num + 10);
        } else {
            reject("실패");
        }
        console.log('작업 완료');
        // resolve('result');
        // reject('실패'); // 실패시, 에러남
    }
        , 1000);
});

console.log(promise);


//resolve의 결과를 가져다 쓰기 then으로 매개변수를 이용해서 사용가능
promise.then((data) => {
    console.log(data);
})

//실패 시
promise.catch((error) => {
    console.log(error);
});


// 이때 저 then, catch은 자기 가신의 객체인 Promise를 반환함 따라서 체인메소드방식 가능

promise.then((data) => {
    console.log(data);
}).catch((error) => {
    console.log(error);
})


//활용

function add10(num) {
    const promise = new Promise((resolve, reject) => {
        //비동기 작업 수행
        setTimeout(() => {

            if (typeof num === "number") {
                resolve(num + 10);
            } else {
                reject("실패");
            }
            console.log('작업 완료');
            // resolve('result');
            // reject('실패'); // 실패시, 에러남
        }
            , 1000);
    });

    return promise;
}

const p = add10(0);
p.then((result) => {
    console.log(result);

    const p2 = add10(result);
    return p2; // then은 원래 자기자신이지만 return값정하면 해당 새로운 프로미스로 연결가능
}).then((result) => {
    console.log(result);
}).catch((error) => { //error는 위의 어느 then이든 해당 error관련해서 처리함.
    console.log(error);
});
















