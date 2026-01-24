select factory_id, factory_name, address
from food_factory
where substring(address, 1,2) = '강원'
order by factory_id;