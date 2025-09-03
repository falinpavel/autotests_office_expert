import allure
from selene import browser, be, have
from selene.core.conditions import Condition


class ComponentHeaderMenu:

    @allure.step("Пользователь нажимает на кнопку 'Контакты'")
    def go_to_contacts_page(self):
        with allure.step("Происходит переход на страницу 'Контакты'"):
            browser.element("""a.top-menu__items[href="/contacts/"]""").should(Condition.by_and(
                be.clickable, have.text("Контакты"))).click()
        return self

    @allure.step("Пользователь нажимает на кнопку 'Оплата'")
    def go_to_payment_page(self):
        with allure.step("Происходит переход на страницу 'Оплата'"):
            browser.element("""a.top-menu__items[href="/info/sposoby-oplaty-zakaza/"]""").should(
                Condition.by_and(be.clickable, have.text("Оплата"))).click()
        return self

    @allure.step("Пользователь нажимает на кнопку 'Доставка'")
    def go_to_delivery_page(self):
        with allure.step("Происходит переход на страницу 'Доставка'"):
            browser.element("""a.top-menu__items[href="/info/sposoby-dostavki/"]""").should(
                Condition.by_and(be.clickable, have.text("Доставка"))).click()
        return self

    @allure.step("Пользователь нажимает на кнопку 'Корзина'")
    def click_cart(self):
        with allure.step("Происходит переход на страницу 'Корзина'"):
            browser.element("""//div[@class="tw-group tw-relative"]//a[@href="/order/"]""").should(
                Condition.by_and(be.clickable, have.text("Корзина"))).click()
        return self

