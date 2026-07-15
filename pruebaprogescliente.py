from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

def inicio_sesion_correcto():
    driver= webdriver.Chrome()
    try:
        driver.get("http://localhost/tecnicelv1")
        time.sleep (5)        
        driver.find_element(By .NAME,"usuario"). send_keys("admin")
        time.sleep (3)
        driver.find_element(By .NAME,"password"). send_keys("1256")
        time.sleep (3)
        driver.find_element(By .CSS_SELECTOR , "button").click()
        time.sleep (3)
        driver.find_element(By .CSS_SELECTOR , "card ").click()
        time.sleep (3)
        mensaje = driver.find_element(By.CSS_SELECTOR, ".card h3").text
        if "Bienvenido admin" in mensaje.lower():
            print("PASS - Test inicio de sesion correcta ")
        else:
            print("FAIL - Test inicio de sesion ")


    finally:
        driver.quit()
inicio_sesion_correcto()