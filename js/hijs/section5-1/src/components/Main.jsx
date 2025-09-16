import "./Main.css"
const Main = () => {
    //{} 안에는 js 한줄로 표현가능한 표현식만 가능함.
    // 숫자, 문자열 배열만 정상적으로 렌더링 됨
    // 최상위 태그는 반드시 하나여야만 한다. 만약 <> </>가 있다면 이는 최상위 태그가 없음을 의미
    const number = 10;
    
    const user = {
        isLogin: false
    }
    
    if (user.isLogin) {
        return (
            <>
            
            <div style={{
                backgroundColor: "red",
            }}>로그인 성공</div>
            </>
        )
    }
    //원래는 class이지만 js에서는 class가 예약어라서 className으로 해야함. 근데 class로 해도 작동은 됨.
    return (
        <main>
            <div className="logout"> logout임</div>
            <h1>main 임</h1>
            <h2>{number + 10}</h2>
            <h2>{number % 2}</h2>
            <h2>{number * 20}</h2>
            <h2>{number * 2 === 20 ? "참" : "거짓"}</h2>
            <h2>{[1, 2, 3]}</h2>
        </main>
    )
};

export default Main;