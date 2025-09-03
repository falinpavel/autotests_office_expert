import allure
import pytest

from helpers.application_manager.application_manager import office_expert


@allure.epic("Корзина пользователя")
@allure.feature("Корзина неавторизованного пользователя")
class TestCheckUserCart:

    @allure.title("Проверка что корзина неавторизованного пользователя пустая")
    @allure.story("При первом посещении сайта корзина неавторизованного пользователя пустая")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("Проверка что пользователь имеет пустую корзину при первом посещении сайта")
    @allure.label("Owner", "AQA Фалин Павел")
    def test_that_unauthorized_user_cart_is_empty(self):
        office_expert.home_page \
            .open() \
            .accept_region_pop_up()
        office_expert.header_menu.click_cart()
        office_expert.cart.check_that_cart_is_empty()
