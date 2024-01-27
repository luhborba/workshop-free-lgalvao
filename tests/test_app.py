from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from time import sleep

# Definindo Driver
driver = webdriver.Firefox()

# Define um timeout
driver.set_page_load_timeout(10) 

# Utilizando Try-Except para entrar na página
try:
    driver.get("http://localhost:8501")
    sleep(5)
    print("Acessando Página com o devido sucesso")
except TimeoutException:
    print("Tempo de Carregamento excedeu todos os limites...")
finally:
    driver.quit()
