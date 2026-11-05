
import pytest

BASE_URL = "http://127.0.0.1:8000/delivery.html"


@pytest.fixture
def delivery_page(page):
    page.goto(BASE_URL)
    page.locator("#amount").wait_for()
    return page
