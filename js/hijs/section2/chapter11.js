// 비동기 setTimeout자체가 비동기적으로 webapi에서 처리됨.
function task(a, b, callback) {
    console.log('task start');
    setTimeout(() => {
        const sum = a + b;
        callback(sum);    
    }, 1000);
    console.log('task end');
}

task(1, 2, (value) => {
    console.log(value);
});













