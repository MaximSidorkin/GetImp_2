import unittest
import time
global str

# import HTMLTestRunner, sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.ui import Select

# global variable
driver = webdriver.Firefox()
driver.get("https://dev.eor.gosapi.ru/site/login")
driver.maximize_window()
time.sleep(3)
wait = WebDriverWait(driver, 40)
driver.implicitly_wait(10)

class ASeleniumLogin_1(unittest.TestCase):
    def test001_LoginInEORDev(self):
        assert "Login" in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
        print('\n1. Логинимся в систему')

    def test002_Not500or404andLoginIsVisible(self):
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        time.sleep(3)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        print("2. Логин пользователя отобажен, страница загружена без ошибок")

    def test003_OpenAllPjct(self):
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(2)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()
        print("3. Переходим в раздел 'Все проекты'")

    def test004_Not500or404(self):
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        print("4. Страница загружена без ошибок")

    def test005_OpenForm(self):
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        time.sleep(3)
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        print("5. По ключевому слову Selenium находим блок")

    def test006_FindBlock(self):
        #находим блок
        findBlock = driver.find_element_by_link_text('Для совещаний Se')
        findBlock.click()
        time.sleep(1)
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        print("6. От блока переходим к проекту")

    def test007_FindCP(self):
        findProject = driver.find_element_by_link_text('Проект для совещаний Se')
        findProject.click()
        time.sleep(2)
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        print("7. От проекта переходим к контрольным точкам")

    def test008_DelCP(self):
        i = 1
        while i < 65:
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[3]')))
            driver.find_element_by_xpath('//button[3]').click()
            driver.find_element_by_xpath('//div[3]/div/button').click()
            print('удалено ',i,' КТ')
            time.sleep(10)
            i = i + 1

    def test009_Fin(self):
        print(' CP deleted')

if __name__ == '__main__':
    unittest.main()
#