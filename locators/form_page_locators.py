from selenium.webdriver.common.by import By

class FormPageLocators:  # эл-ты страницы, которые будут "участвовать" в тестировании
    LOGIN = (By.CSS_SELECTOR, '#user-name')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login-button')
    ERROR_BUTTON = (By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3")

