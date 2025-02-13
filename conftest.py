import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()  # декоратор, расширяющий возможности функции
def driver():
    driver_service = Service(ChromeDriverManager().install())  # управление драйвером Хрома
    driver = webdriver.Chrome(service=driver_service)  # присваиваем переменной инициализацию драйвера
    driver.maximize_window()
    yield driver  # разделитель, до него выполняется тест, остальное после него
    driver.quit()
