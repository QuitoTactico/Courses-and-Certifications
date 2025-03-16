def calculate_total(products, discount_coupon):
    total = 0
    for product in products:
        total += (product["price"] - (discount_coupon * product["price"]))
    return total


def test_calculate_total_with_empty_list():
    print("Test passed 1")
    assert calculate_total([],0) == 0


def test_calculate_total_with_single_product():
    products = [{"name": "Product 1", "price": 10}]
    print("Test passed 2")
    assert calculate_total(products,0.10) == 9


def test_calculate_total_with_multiple_products():
    products = [{"name": "Product 1", "price": 10}, {"name": "Product 2", "price": 20}]
    print("Test passed 3")
    assert calculate_total(products,0.10) == 27


if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_products()
