import allure
from selene import browser, be, have
from selene.core.conditions import Condition


class ComponentCart:
    """
    Class for working with the cart methods
    """
    @allure.step("Проверка, что корзина пустая")
    def check_that_cart_is_empty(self):
        with allure.step("Проверка, что корзина пуста"):
            browser.element("""//h2[text()="Корзина пуста"]""").should(
                Condition.by_and(be.visible, have.text("Корзина пуста")))
        return self
