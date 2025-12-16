select warehouse_id, warehouse_name, address, coalesce(freezer_yn, 'N')
from food_warehouse
where substring(address, 1,3) = '경기도'
order by warehouse_id