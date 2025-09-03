import allure
from selene import browser, be, have
from selene.core.conditions import Condition

from helpers.data.links import Links


class ContactsPage:
    """
    Page object for the contacts page,
    contains methods for working with the contacts page

    Pattern Fluent Page Object (return self)
    """

    def __init__(self):
        self.url = Links.CONTACTS_URL

    @allure.step("Происходит переход на страницу 'Контакты'")
    def open(self):
        with allure.step(f"Страница {self.url}"):
            browser.open(self.url)
        return self

    @allure.step("Происходит проверка открытия страницы 'Контакты'")
    def is_opened(self):
        with allure.step("Проверяет что страница открыта"):
            browser.element("""//h3[contains(text(),'Контактная информация')]""").should(Condition.by_and(
                be.clickable, have.text("Контактная информация")))
