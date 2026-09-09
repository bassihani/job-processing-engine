from job_processing_engine.customer import Customer


def test_customer_object_creation():
    customer = Customer(1, "John", "john.tesla@gmail.com", True)
    assert customer.name == "John"
    assert customer.id == 1
    assert customer.is_active is True