from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

def tex():
    driver= webdriver.Chrome()
    try:
        driver.get("https://the-internet.herokuapp.com/")
        time.sleep (3)
        driver.find_element(By .LINK_TEXT,"Form Authentication"). click()
        time.sleep (3)
        driver.find_element(By .ID,"username"). send_keys("tomsmith")
        time.sleep (3)
        driver.find_element(By .ID,"password"). send_keys("SuperSecretPassword!")
        time.sleep (3)
        driver.find_element(By .CSS_SELECTOR , "button").click()
        time.sleep (3)
        mensaje= driver.find_element(By.ID,"flash").text
        if "you logged into a secure area!" in mensaje.lower():
            print("PASS - Test inicio de sesion correcta ")
        else:
            print("FAIL - Test inicio de sesion ")


    finally:
        driver.quit()
inicio_sesion_correcto()

