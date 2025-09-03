import allure
import pytest

from helpers.application_manager.application_manager import office_expert


@allure.epic("Покавая панель")
@allure.feature("Навигация по каталогу через боковую панель")
class TestLeftPanelIsPresent:

    @allure.title("Проверка наличия боковой панели")
    @allure.story("Пользователь при наведении на группу может перейти в подкатегории")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("Проверка наличия боковой панели и возможность навигации по каталогу")
    @allure.label("Owner", "AQA Фалин Павел")
    @pytest.mark.parametrize(
        "catalog_group_name",
        ["Бумага и бумажная продукция", "Канцелярские товары",
         "Хозяйственные товары", "Продукты питания", "Техника и электроника",
         "Картриджи и тонер", "Мебель и интерьер", "Подарки и сувениры", "Товары для творчества и учебы"],
        ids=
        ["Paper and paper products", "Stationery",
         "Household goods", "Food", "Equipment and electronics",
         "Cartridges and toner", "Furniture and interior", "Gifts and souvenirs", "Goods for creativity and study"])
    def test_hover_on_main_catalog_group_in_left_panel(self, catalog_group_name):
        office_expert.home_page \
            .open() \
            .accept_region_pop_up()
        office_expert.left_panel.hover_on_catalog_group(catalog_group_name)
