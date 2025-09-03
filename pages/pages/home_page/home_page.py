import allure
from selene import browser, be, have
from selene.core.conditions import Condition

from helpers.data.links import Links


class HomePage:
    """
    Page object for the home page,
    contains methods for working with the home page
    """
    def __init__(self):
        self.url = Links.BASE_URL

    @allure.step("Происходит переход на страницу 'Главная'")
    def open(self):
        with allure.step(f"Страница {self.url}"):
            browser.open(self.url)
        return self

    @allure.step("Происходит принятие поп-апа с указанием предопределенного региона")
    def accept_region_pop_up(self):
        with allure.step("Нажимаем на кнопку 'Да'"):
            browser.element("""//button[text()="Да"]""").should(Condition.by_and(
                be.clickable, have.text("Да"))).click()
        return self
