from selenium.webdriver.common.by import By

class CheckoutPageLocators:
    FIRST = (By.CSS_SELECTOR, '#first-name')
    LAST = (By.CSS_SELECTOR, '#last-name')
    POSTAL_CODE = (By.CSS_SELECTOR, '#postal-code')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '#continue')
    FINISH_BUTTON = (By.CSS_SELECTOR, '#finish')
    COMPLETE_HEADER = (By.CSS_SELECTOR, '.complete-header')