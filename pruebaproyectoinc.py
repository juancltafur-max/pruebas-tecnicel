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

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , ".container .card .btn.btn-danger"))
        ).click()       
      

        assert "http://localhost/tecnicelv1/dashboard/dashboard.php" in driver.current_url

        print("¿Eliminar este cliente y sus equipos/reparaciones asociadas?")
        

    finally:
        driver.quit()