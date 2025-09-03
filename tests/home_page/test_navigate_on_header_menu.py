import allure

from helpers.application_manager.application_manager import office_expert


@allure.epic("Верхнее меню")
@allure.feature("Навигация по сайту через верхнее меню")
class TestNavigateOnHeaderMenu:

    @allure.title("Пользователь может перейти на страницу 'Контакты'")
    @allure.story("Пользователь при клике на кнопку 'Контакты' переходит на страницу контактов")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Пользователь нажимает на кнопку 'Контакты' и переходит на страницу контактов")
    @allure.label("Owner", "AQA Фалин Павел")
    def test_navigate_to_contacts_page(self):
        office_expert.home_page \
            .open() \
            .accept_region_pop_up()
        office_expert.header_menu.go_to_contacts_page()

    @allure.title("Пользователь может перейти на страницу 'Оплаты'")
    @allure.story("Пользователь при клике на кнопку 'Оплаты' переходит на страницу оплаты")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Пользователь нажимает на кнопку 'Оплаты' и переходит на страницу оплаты")
    @allure.label("Owner", "AQA Фалин Павел")
    def test_navigate_to_payment_page(self):
        office_expert.home_page \
            .open() \
            .accept_region_pop_up()
        office_expert.header_menu.go_to_payment_page()

    @allure.title("Пользователь может перейти на страницу 'Доставка'")
    @allure.story("Пользователь при клике на кнопку 'Доставка' переходит на страницу доставки'")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Пльзователь нажимает на кнопку 'Доставка' и переходит на страницу доставки")
    @allure.label("Owner", "AQA Фалин Павел")
    def test_navigate_to_delivery_page(self):
        office_expert.home_page \
            .open() \
            .accept_region_pop_up()
        office_expert.header_menu.go_to_delivery_page()
