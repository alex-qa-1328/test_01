import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# TODO: Модуль 12. Основы Selenium
'''
1. Скачать и установить библиотеку selenium
pip install selenium
2. Скачать сам драйвер браузера Хром (chromedriver)
googlechromelabs.github.io/chrome-for-testing/#stable
3. Переместить хромдрайвер в проект, скопировать путь до него
'''

user_login = "mytestuserforotsdsdz"
user_pass = "ASDh1297yasdS@&#^"

web_element = driver.find_element(By.XPATH)
enter_button = "//a[@class='home-link2 headline__personal-enter home-link2_color_black']"
login_field = "//*[@id='id_login']" # XPATH локатор
login_field_id = 'id_login' # ID локатор
email_field = 'id_mail' # ID локатор
pass_field_name = 'pass' # ID локатор

driver = webdriver.Chrome()
url = "https://ya.ru"

driver.maximize_window()

driver.get(url)



time.sleep(5)

driver.find_element(By.XPATH, enter_button).click() # XPATH наиболее универсальный после ID


# driver.find_element(By.ID)  # самый стабильный и приоритетный локатор
# driver.find_element(By.NAME)
# driver.find_element(By.TAG_NAME)
# driver.find_element(By.LINK_TEXT)
# driver.find_element(By.CLASS_NAME)



driver.quit()


# @pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options)
    yield driver
    driver.quit()

def test_login(driver):
    # driver.get(url)


    assert driver.find