from main import hello


def test_hello_full_name():
    assert hello(firstname="John", lastname="Doe") == "Hello, John Doe!"
