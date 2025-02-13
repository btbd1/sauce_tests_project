from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver): #определяем,что для работы каждый раз нужны драйвер и адрес страницы
        self.driver = driver
        # self.url = url

    def open(self, url): #функция открытия страницы
        self.driver.get(url)

    def element_is_visible(self, locator, timeout=5): #для ситуаций,требующих небольшого ожидания загрузки элементов
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator)) #подожди, пока указанный элемент не станет видимым

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def get_children_element(self, parent_locator, children_locator):
        parent_element = self.driver.find_element(*parent_locator)
        if not parent_element:
            raise Exception(f"Parent element not found for locator: {parent_locator}")
        return parent_element.find_elements(*children_locator)