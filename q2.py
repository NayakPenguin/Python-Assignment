coupons = {
        "MON": 0.1, 
        "TUE": 0.15,
        "WED": 0.2, 
        "THU": 0.25,
        "FRI": 0.3, 
        "SAT": 0.15,
        "SUN": 0.1, 
    }

def apply_discount(coupon_code, amount):
    if coupon_code in coupons:
        discount_rate = coupons[coupon_code]
        discount_amount = amount * discount_rate
        discounted_price = amount - discount_amount
        print(f"Discounted price: ${discounted_price:.2f}")
    else:
        print("Invalid coupon code.")


coupon_code = input("Enter the coupon code: ")
amount = float(input("Enter the original amount: $"))
apply_discount(coupon_code, amount)
