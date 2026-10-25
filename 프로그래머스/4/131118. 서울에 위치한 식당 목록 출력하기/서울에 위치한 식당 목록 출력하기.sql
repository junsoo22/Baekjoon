-- 코드를 입력하세요
SELECT a.rest_id, a.rest_name, a.food_type, a.favorites, a.address, round(avg(b.review_score),2) as score
from rest_info a, rest_review b
where address like '서울%'
and a.rest_id = b.rest_id
GROUP BY
    a.REST_ID,
    a.REST_NAME,
    a.FOOD_TYPE,
    a.FAVORITES,
    a.ADDRESS
order by score desc, a.favorites desc;