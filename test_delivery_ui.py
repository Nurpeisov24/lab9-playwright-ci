
import pytest


def calculate(page, amount, delivery_type):
    page.locator("#amount").fill(str(amount))
    page.locator("#delivery").select_option(delivery_type)
    page.locator("#calculate").click()
    return page.locator("#result").inner_text()


@pytest.mark.parametrize(
    "amount,delivery_type,expected_delivery",
    [
        (0, "city", 1000),
        (1, "city", 1000),
        (5000, "city", 1000),
        (9999, "city", 1000),
        (10000, "city", 0),
        (15000, "city", 0),
        (0, "region", 2000),
        (1, "region", 2000),
        (5000, "region", 2000),
        (9999, "region", 2000),
        (10000, "region", 0),
        (15000, "region", 0),
    ],
)
def test_delivery_calculation(
    delivery_page,
    amount,
    delivery_type,
    expected_delivery,
):
    result = calculate(
        delivery_page,
        amount,
        delivery_type,
    )

    expected_total = amount + expected_delivery

    assert (
        f"Стоимость доставки: {expected_delivery} ₸."
        in result
    )

    assert f"Итого: {expected_total} ₸" in result
