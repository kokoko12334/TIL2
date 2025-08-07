


// function waitAndRun() {
//     setTimeout(()=> {
//         console.log("end");
//     }, 2000);
// }

// waitAndRun();


// const timeoutPromise = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         resolve('완료');
//     }, 2000);
// });


// // Promise객체의 resolve의 인자값을 res로 하는 것을 받아서 처리하는 것이 then
// timeoutPromise.then((res) => {
//     console.log('then')
//     console.log(res);
// });

const getPromise =  (seconds) => new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('완료' + seconds);
    }, seconds * 1000);
});


// getPromise(1)
// .then((res) => {
//     console.log(res);
//     return getPromise(3);
// }).then((res) => {
//     console.log(res);
//     return getPromise(2);
// }).then((res) => {
//     console.log(res);
// });




const getPromise2 =  (seconds) => new Promise((resolve, reject) => {
    setTimeout(() => {
        if (seconds == 1) {
            resolve('완료');
        }
        reject('에러');
    }, seconds * 1000);
});


// getPromise2(2).then((res) => {
//     console.log(res);
// }).catch((res) => {
//     console.log(res);
// })



// 실행은 동시에 되고 모든 작업이 완료되어야 then이 실행 즉 최대로 오래걸린시간기준으로 해당 all메소드가 완료됨.
Promise.all([
    getPromise(3),
    getPromise(1),
    getPromise(2),
    
]).then((res) =>{
    console.log(res);
}).catch((res) => {
    console.log(res);
});









