
SELECT TO_CHAR(sales_date, 'YYYY-MM-DD') AS sales_date,
       product_id,
       user_id,
       sales_amount
FROM online_sale
WHERE sales_date >= DATE '2022-03-01'
  AND sales_date < DATE '2022-04-01'

UNION ALL

SELECT TO_CHAR(sales_date, 'YYYY-MM-DD') AS sales_date,
       product_id,
       NULL AS user_id,
       sales_amount
FROM offline_sale
WHERE sales_date >= DATE '2022-03-01'
  AND sales_date < DATE '2022-04-01'

ORDER BY sales_date ASC, product_id ASC, user_id ASC;
