from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_correcto():
    driver = webdriver.Chrome()


    try:
    
        driver.get ("https://the-internet.herokuapp.com/")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT,"Form Authentication"))
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID,"username")) 
        ). send_keys("tomsmith")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID,"password")) 
        ). send_keys("SuperSecretPassword!")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , "button"))
        ).click()       

        mensaje= WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID,"flash"))
        ).text

        assert "you logged into a secure area!" in mensaje.lower()

        print("PASS - Test inicio de sesion correcta ")

    finally:
        driver.quit()