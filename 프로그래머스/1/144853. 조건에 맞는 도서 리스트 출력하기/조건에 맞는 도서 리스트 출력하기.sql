-- 코드를 입력하세요
SELECT book_id, published_date
from book
where published_date like '2021%'
and category = '인문'
;