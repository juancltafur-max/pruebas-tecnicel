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
        driver.find_element(By .NAME,"password"). send_keys("1234")
        time.sleep (3)
        driver.find_element(By .CSS_SELECTOR , "button").click()
        time.sleep (3)
        try:
            mensaje = driver.find_element(By.CSS_SELECTOR, ".card h3").text
            if "Bienvenido admin" in mensaje.lower():
                print("FAIL - Se inició sesión con credenciales incorrectas (Error de seguridad)")
            else:            
                print("FAIL - Test inicio de sesion (Entró a otra pantalla inesperada)")
        except:
           
            print("PASS - Test inicio de sesion rechazada (Usuario o contraseña incorrecta)")

    finally:
        
        time.sleep(3)
        driver.quit()

inicio_sesion_correcto()