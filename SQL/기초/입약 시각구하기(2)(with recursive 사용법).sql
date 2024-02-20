-- 코드를 입력하세요

WITH RECURSIVE cte_count 
AS ( 
    
    SELECT 0 AS n    -- 처음의 초기값 => n열에 0값 하나만
    
    UNION ALL
    
    SELECT n + 1 AS n -- 0+1 인 n열에 값 구하고 위에서 unionall로 합쳐줌 
    FROM cte_count     -- 테이블 에서
    WHERE n <  23      --  while문 처음 해당 조건 만족하면 계속 반복  즉, 마지막에 22에서 22+1까지는 만듷어지고 그다음 23은 조건 만족하지 못하므로 recursive 빠져나감
)

SELECT H.N, IF(C.CNT IS NOT NULL, C.CNT, 0) AS COUNT
FROM CTE_COUNT AS H
LEFT JOIN 
(SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS CNT FROM ANIMAL_OUTS GROUP BY HOUR(DATETIME) ORDER BY HOUR(DATETIME)) AS C
ON C.HOUR = H.N