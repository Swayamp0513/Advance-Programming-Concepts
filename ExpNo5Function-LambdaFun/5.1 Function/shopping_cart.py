cart = {}

def add_product(name, price, quantity):
    cart[name] = {'price': price, 'quantity': quantity}

def remove_product(name):
    if name in cart:
        del cart[name]




def calculate_subtotal():
    subtotal = 0
    for item in cart.values():
        subtotal += item['price'] * item['quantity']
    return subtotal

def generate_invoice(coupon_discount_percent=0):
    subtotal = calculate_subtotal()
    discount = subtotal * (coupon_discount_percent / 100)
    gst = (subtotal - discount) * 0.18
    return subtotal - discount + gst

add_product("Shirt", 500, 2)
add_product("Pants", 1000, 1)
print("Final Invoice Amount:", generate_invoice(10))
