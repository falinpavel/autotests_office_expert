import allure
from selene import browser, be, have
from selene.core.conditions import Condition


class ComponentLeftPanel:
    """
    Component object for the left panel,
    contains methods for working with the left panel

    Pattern Fluent Page Object (return self)
    """

    @allure.step("Пользователь наводит курсор на группу каталога")
    def hover_on_catalog_group(self, catalog_group_name: str):
        with allure.step(f"Наводит на группу {catalog_group_name}"):
            browser.element(f"""//span[contains(text(),'{catalog_group_name}')]""").should(Condition.by_and(
                be.clickable, have.text(catalog_group_name))).hover()
        return self
