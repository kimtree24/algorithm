select product_code, (p.price * o.sales_amount ) as sales
from product as p
join
    (select product_id, sum(sales_amount) as sales_amount
    from offline_sale
    group by product_id) as o
    on p.product_id = o.product_id
group by p.product_code
order by sales desc, product_code;