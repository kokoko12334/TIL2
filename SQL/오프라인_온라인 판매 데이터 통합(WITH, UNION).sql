WITH O AS(
    SELECT DATE_FORMAT(SALES_DATE,'%Y-%m-%d') AS DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT 
    FROM ONLINE_SALE 
    WHERE SALES_DATE LIKE '2022-03%'),
    
    F AS(
    SELECT DATE_FORMAT(SALES_DATE,'%Y-%m-%d') AS DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT 
    FROM OFFLINE_SALE 
    WHERE SALES_DATE LIKE '2022-03%')
    

SELECT *
FROM
(SELECT * FROM O UNION SELECT * FROM F) AS K
ORDER BY DATE, PRODUCT_ID, USER_ID




-- WITH은 ,로 여러개 생성 가능 UNION으로 위아래로 그냥 붙힐 수 있음.