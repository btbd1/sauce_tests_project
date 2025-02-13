from pages.base_page import BasePage
from locators.cart_page_locators import CartPageLocators as Locators
from locators.checkout_pages_locators import CheckoutPageLocators


class CheckoutPages(BasePage):
    def fill_checkout_fields_right(self):
        self.find_element(CheckoutPageLocators.FIRST).send_keys('Test')
        self.find_element(CheckoutPageLocators.LAST).send_keys('User')
        self.find_element(CheckoutPageLocators.POSTAL_CODE).send_keys('12345')
        self.find_element(CheckoutPageLocators.CONTINUE_BUTTON).click()

    def finish_checkout_successful(self):
        self.find_element(CheckoutPageLocators.FINISH_BUTTON).click()
        complete_header_text = self.find_element(CheckoutPageLocators.COMPLETE_HEADER).text
        assert complete_header_text == 'Thank you for your order!', f'Successful checkout message not found!'
