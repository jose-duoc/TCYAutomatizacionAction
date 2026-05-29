from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
 
def ejecutar_prueba_sistema(): 
    #Configurar navegador
    options =  Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    
    
    try:
        #abrir sistema
        driver.get("https://fundacion-instituto-profesional-duoc-uc.github.io/APIAutos/index.html")
        driver.maximize_window()
    
    
        #mantener abierto el navegador
        time.sleep(2)
        #validar título
        print("Título de la página:", driver.title)
        titulo = driver.title
        #Buscar campos del formulario
        inputs = driver.find_elements(By.TAG_NAME, "input")
        botones = driver.find_elements(By.TAG_NAME, "button")
    
        driver.save_screenshot("Evidencia.png")
        detalle = f"""
                Paso a paso ejecutado:
                1. Se abrió la URL correctamente.
                2. Título obtenido: {titulo}
                3. Inputs encontrados: {len(inputs)}
                4. Botones encontrados: {len(botones)}
                5. La página cargó correctamente.
                """
        print(f"campos encontrados: {len(inputs)}")
        print(f"botones encontrados:{len(botones)}")
        if len(inputs) > 0 or len(botones) > 0:
            mensaje = "Prueba Exitosa: El sistema cargó correctamente"
            print(mensaje)
            return True,mensaje,detalle
        else:
            mensaje = "Prueba Fallida: no se encontraron los elementos"
            print(mensaje)
            return False, mensaje
        
    except Exception as e:
        print("error durante la prueba:",e)
    finally:
        driver.quit()