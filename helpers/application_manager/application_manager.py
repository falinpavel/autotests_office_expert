from pages.components.cart.component_cart import ComponentCart
from pages.components.header.component_header_menu import ComponentHeaderMenu
from pages.components.left_panel.component_left_panel import ComponentLeftPanel
from pages.pages.contacts_page.contacts_page import ContactsPage
from pages.pages.home_page.home_page import HomePage


class ApplicationManager:
    def __init__(self):
        self.header_menu = ComponentHeaderMenu()
        self.left_panel = ComponentLeftPanel()
        # self.footer = ComponentFooter()
        self.cart = ComponentCart()
        self.home_page = HomePage()
        self.contacts_page = ContactsPage()
        # self.payment_page = PaymentPage()
        # self.delivery_page = DeliveryPage()


office_expert = ApplicationManager()
