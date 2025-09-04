//콜백함수 -> 인자에 함수가 간거
function main(value) {
    
    value();
}

function value() {
    console.log("sub function");
}

main(value);

main(() => {console.log("DDDD")});



function repeat(count, callback) {
    for (let idx=1; idx <=count; idx++) {
        callback(idx);
    }
}



repeat(5, (idx) => {console.log(idx *3)});










