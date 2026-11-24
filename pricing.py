LIBRARY_VERSION = "1.0.0"
DISCOUNT_RATE = 0.10


def calculate_net_amount(amount):
    return round(float(amount) * (1 - DISCOUNT_RATE), 2)
