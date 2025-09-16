# -- 코드를 입력하세요
SELECT b.title, b.board_id, r.reply_id, r.writer_id,r.contents,date_format(R.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
from used_goods_board b
join used_goods_reply r on b.board_id=r.board_id 
where year(b.created_date)='2022' and month(b.created_date)='10'
order by r.created_date asc, b.title asc;
