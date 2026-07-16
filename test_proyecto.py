from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_admin_correcto():
    driver = webdriver.Chrome()


    try:
    
        driver.get ("http://localhost/tecnicelv1")

               
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"usuario")) 
        ). send_keys("admin")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"password")) 
        ). send_keys("123456")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , "button"))
        ).click()       

        mensaje= WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".card h3"))
        ).text

        assert "bienvenido admin" in mensaje.lower()

        print("PASS - Test inicio de sesion correcta ")

    finally:
        driver.quit()


def test_login_admin_incorrecto():
    driver = webdriver.Chrome()


    try:
    
        driver.get ("http://localhost/tecnicelv1")

               
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"usuario")) 
        ). send_keys("admin")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"password")) 
        ). send_keys("1234")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , "button"))
        ).click()       

        mensaje= WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        ).text

        assert "usuario o contraseña incorrectos" in mensaje.lower()

        print("PASS - Test inicio de sesion incorrecta ")

    finally:
        driver.quit()


def test_Clientes_Nuevo_Cliente():
    driver = webdriver.Chrome()


    try:
    
        driver.get ("http://localhost/tecnicelv1")

               
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"usuario")) 
        ). send_keys("admin")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"password")) 
        ). send_keys("123456")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , "button"))
        ).click()  

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , ".container .card .btn.btn-primary"))
        ).click()       

        mensaje= WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR , ".navbar"))
        ).text

        assert "clientes" in mensaje.lower()

        print("PASS - Test inicio de sesion Clientes Nuevo ")

    finally:
        driver.quit()

def test_Clientes_Nuevo_Cliente_Guardar():
    driver = webdriver.Chrome()


    try:
    
        driver.get ("http://localhost/tecnicelv1")

               
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"usuario")) 
        ). send_keys("admin")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"password")) 
        ). send_keys("123456")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , "button"))
        ).click()  

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , ".container .card .btn.btn-primary"))
        ).click()  

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , ".container .card .btn.btn-primary"))
        ).click()        

        mensaje= WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "nombre" ))
        ).send_keys ("julian")
        
        mensaje= WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "correo" ))
        ).send_keys ("julian@gmail.com")

        mensaje= WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "telefono" ))
        ).send_keys ("3508354940")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form button"))
        ).click()    

        assert "listar.php" in driver.current_url

        print("¡Prueba exitosa! El cliente fue guardado de manera correcta.")
        

    finally:
        driver.quit()

def test_Clientes_Eliminar_Nuevo_Cliente ():
    driver = webdriver.Chrome()


    try:
    
        driver.get ("http://localhost/tecnicelv1")

               
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"usuario")) 
        ). send_keys("admin")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"password")) 
        ). send_keys("123456")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , "button"))
        ).click()  

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , ".container .card .btn.btn-primary"))
        ).click()  

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , ".container .card .btn.btn-danger"))
        ).click()       
      

        assert "dashboard.php" in driver.current_url

        print("¿Eliminar este cliente y sus equipos/reparaciones asociadas?")
        

    finally:
        driver.quit()


def test_rol_tecnico_correcto():
    driver = webdriver.Chrome()


    try:
    
        driver.get ("http://localhost/tecnicelv1")

               
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"usuario")) 
        ). send_keys("tecnico1")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"password")) 
        ). send_keys("123456")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , "button"))
        ).click()       

        mensaje= WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".card h3"))
        ).text

        assert "bienvenido técnico uno" in mensaje.lower()

        print("PASS - Test inicio rol tecnico correcta ")

    finally:
        driver.quit()   


def test_rol_recepcion_correcto():
    driver = webdriver.Chrome()


    try:
    
        driver.get ("http://localhost/tecnicelv1")

               
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"usuario")) 
        ). send_keys("recepcion1")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"password")) 
        ). send_keys("123456")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , "button"))
        ).click()       

        mensaje= WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".card h3"))
        ).text

        assert "bienvenido recep" in mensaje.lower()

        print("PASS - Test inicio rol recep correcta ")

    finally:
        driver.quit()   

def test_rol_admin_ver_reparacion():
    driver = webdriver.Chrome()


    try:
    
        driver.get ("http://localhost/tecnicelv1")

               
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"usuario")) 
        ). send_keys("admin")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"password")) 
        ). send_keys("123456")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , "button"))
        ).click()  

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , ".container .card .btn.btn-success"))
        ).click()  

        mensaje= WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR , ".navbar"))
        ).text

        assert "reparaciones" in mensaje.lower()

        print("PASS - Test reparaciones ")

    finally:
        driver.quit()

def test_rol_admin_ver_inventario():
    driver = webdriver.Chrome()


    try:
    
        driver.get ("http://localhost/tecnicelv1")

               
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"usuario")) 
        ). send_keys("admin")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"password")) 
        ). send_keys("123456")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , "button"))
        ).click()  

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , ".container .card .btn.btn-primary"))
        ).click()  

        mensaje= WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR , ".navbar"))
        ).text

        assert "clientes" in mensaje.lower()

        print("PASS - Test - Inventario_Repuestos ")

    finally:
        driver.quit()

def test_rol_admin_ver_inventario_proveedores():
    driver = webdriver.Chrome()


    try:
    
        driver.get ("http://localhost/tecnicelv1")

               
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"usuario")) 
        ). send_keys("admin")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"password")) 
        ). send_keys("123456")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , "button"))
        ).click()  

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , ".container .card .btn.btn-warning"))
        ).click()  

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , ".container .card .btn.btn-warning"))
        ).click()  

        mensaje= WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR , ".navbar"))
        ).text

        assert "inventario - proveedores" in mensaje.lower()

        print("PASS - Test - Inventario_proveedor ")

    finally:
        driver.quit()
