from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators
from locators.inventory_page_locators import InventoryPageLocators

class FormPage(BasePage):  # наследуем от другого класса

    def fill_fields_correct(self):
        login = 'standard_user'
        password = 'secret_sauce'
        self.element_is_visible(Locators.LOGIN).send_keys(login)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.LOGIN_BUTTON).click()
        # assert 'inventory' in self.driver.current_url, f'Wrong page!'
        assert self.find_element(InventoryPageLocators.CURRENT_TITLE).text == 'Products', f'Title "Products" not found!'

    def fill_fields_incorrect(self):
        incorrect_login = 'wrong_user'
        incorrect_password = 'wrong_password'
        self.element_is_visible(Locators.LOGIN).send_keys(incorrect_login)
        self.element_is_visible(Locators.PASSWORD).send_keys(incorrect_password)
        self.element_is_visible(Locators.LOGIN_BUTTON).click()

    def find_error_button(self):
        elements = self.find_elements(Locators.ERROR_BUTTON)
        if elements:
            assert f"{elements[0].text}" == 'Epic sadface: Username and password do not match any user in this service'
        else:
            return "Element not found!"
