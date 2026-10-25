-- 코드를 입력하세요
SELECT count(*) as users
from user_info
WHERE JOINED >= DATE '2021-01-01'
  AND JOINED < DATE '2022-01-01'
and age between 20 and 29