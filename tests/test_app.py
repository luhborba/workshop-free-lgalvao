from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from time import sleep
import pytest
import subprocess

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
    sleep(10)
