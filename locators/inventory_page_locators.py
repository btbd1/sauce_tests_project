from selenium.webdriver.common.by import By


class InventoryPageLocators:
    CURRENT_TITLE = (By.CLASS_NAME, 'title')
    BUTTON_BACKPACK = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
    BUTTON_BIKE_LIGHT = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bike-light')
    BUTTON_CART = (By.CSS_SELECTOR,  '.shopping_cart_link')
