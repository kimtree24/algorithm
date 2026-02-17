select substring(product_code, 1, 2), count(*) as products
from product
group by substring(product_code, 1, 2)
order by substring(product_code, 1, 2)
