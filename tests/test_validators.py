from src.validators import validate_product

def test_valid_product():
    record = {
        "product_id": "123",
        "title": "Test Book",
        "image_path": "/images/test.jpg",
        "image_url": "http://example.com/img.jpg",
        "price": "£10.99",
        "rating": 4,
        "source": "test",
    }

    is_valid, cleaned = validate_product(record)
    assert is_valid
    assert cleaned["price"] == 10.99