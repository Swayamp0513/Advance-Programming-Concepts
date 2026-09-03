from products.item_info import get_item
from customers.profile import get_profile
from orders.cart import calculate_total
from payments.invoice import generate_bill

item = get_item("SKU_99")
cust = get_profile("C77")
total = calculate_total([item["price"], 150])
print(generate_bill("ORD1001", total))
