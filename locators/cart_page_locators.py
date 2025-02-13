from selenium.webdriver.common.by import By


class CartPageLocators:
    ITEM_BACKPACK = (By.CSS_SELECTOR, '#item_4_title_link .inventory_item_name')
    ITEM_BIKE_LIGHT = (By.CSS_SELECTOR, '#item_0_title_link .inventory_item_name')
    BACKPACK_QUANTITY = (By.CSS_SELECTOR, 'div.cart_list > div:nth-child(3) > div.cart_quantity')
    BIKE_LIGHT_QUANTITY = (By.CSS_SELECTOR, 'div.cart_list > div:nth-child(4) > div.cart_quantity')
    REMOVE_BIKE_LIGHT_BUTTON = (By.CSS_SELECTOR, '#remove-sauce-labs-bike-light')
    CART_BADGE = (By.CSS_SELECTOR, '.shopping_cart_badge')  # присутствует при наличии товара в корзине
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, '#checkout')
