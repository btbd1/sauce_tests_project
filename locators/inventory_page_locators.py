from selenium.webdriver.common.by import By


class InventoryPageLocators:
    CURRENT_TITLE = (By.CLASS_NAME, 'title')
    BUTTON_BACKPACK = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
    BUTTON_BIKE_LIGHT = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bike-light')
    BUTTON_CART = (By.CSS_SELECTOR,  '.shopping_cart_link')
    SORT_BUTTON_LOW_HIGH = (By.CSS_SELECTOR, '.product_sort_container [value="lohi"]')
    ITEM_PRICE = (By.CSS_SELECTOR, '.inventory_item_price')
