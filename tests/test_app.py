from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest
import subprocess
import os

@pytest.fixture
def driver():
    # Iniciando o Streamlit através do Subprocess
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])

    # Iniciando o WebDriver
    driver = webdriver.Firefox()
    driver.set_page_load_timeout(10)
    yield driver

    # Fechar o WebDriver
    driver.quit()
    process.kill()

def test_app_open(driver):
    # Verificando se a página abre
    driver.get("http://localhost:8501")
    sleep(8)

def test_app_title(driver):
    # Testando acesso
    driver.get("http://localhost:8501")
    sleep(8)
    # Capturando Título
    page_title = driver.title
    # Verificando se o título confere
    title = "Validador Excel"
    assert page_title == title

def test_app_h1(driver):
    # Testando acesso
    driver.get("http://localhost:8501")
    sleep(8)

    # Capturando primeiro h1
    h1 = driver.find_element(By.TAG_NAME, "h1")

    # Verificando compatibilidade
    texto = "Sistema de Envio de informações para o Domino PMJP-SMS"
    assert h1.text == texto

def test_app_insert_excel(driver):
    # Testando acesso
    driver.get("http://localhost:8501")
    sleep(5)
    
    sucess_file_path = os.path.abspath("data/planilha_vendas.xlsx")
    driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(sucess_file_path)

    sleep(4)
    assert "A estrutura do arquivo está Correta" in driver.page_source