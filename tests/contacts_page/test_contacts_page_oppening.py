import allure
import pytest

from helpers.application_manager.application_manager import office_expert


@allure.epic("Страница 'Контакты'")
@allure.feature("Переход на страницу 'Контакты'")
class TestContactsPageOpening:

    @allure.title("Проверка перехода на страницу 'Контакты'")
    @allure.story("Пользователь может перейти на страницу 'Контакты'")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("Проверка корректного перехода на страницу 'Контакты'")
    @allure.label("Owner", "AQA Фалин Павел")
    def test_contacts_page_opening(self):
        office_expert.home_page \
            .open() \
            .accept_region_pop_up()
        office_expert.header_menu.go_to_contacts_page()
        office_expert.contacts_page.is_opened()
