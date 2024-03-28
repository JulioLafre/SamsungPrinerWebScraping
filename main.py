from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from time import sleep
from impressoras import Impressora4070, Impressora4080, Impressora4020

options = Options()
#options.add_argument("--headless")
options.add_argument('-width=1600')
options.add_argument('-height=900')

# Configuração inicial do navegador
navegador = webdriver.Firefox(options=options)


impressora = None

try:
    navegador.get("http://10.1.3.201/sws/index.html")
    sleep(5)

    try:
        # Tenta identificar a Impressora4070
        navegador.find_element(By.XPATH, "//span[text()='SL-M4070FR']")
        impressora = Impressora4070(navegador)
    except NoSuchElementException:
        pass  # Se não encontrar, prossegue para a próxima tentativa

    try:
        # Tenta identificar a Impressora4080 se a 4070 não foi identificada
        if not impressora:
            navegador.find_element(By.ID, "sws_topMenuName_Information")
            impressora = Impressora4080(navegador)
    except NoSuchElementException:
        pass

    try:
        # Tenta identificar a Impressora4020 se a 4070 e 4080 não foram identificadas
        if not impressora:
            navegador.find_element(By.XPATH, "//span[text()='SL-M4020ND']")
            impressora = Impressora4020(navegador)
    except NoSuchElementException:
        pass

    if not impressora:
        print("Modelo de impressora não reconhecido.")

    # Verificação e execução baseada no tipo de impressora
    if isinstance(impressora, Impressora4070):
        # Código específico para Impressora4070
        print(impressora.modelo_impressora)
        pass

    elif isinstance(impressora, Impressora4080):
        # Código específico para Impressora4080
        print(impressora.modelo_impressora)
        pass
    
    elif isinstance(impressora, Impressora4020):
        # Código específico para Impressora4020
        print(impressora.modelo_impressora)
        pass

finally:
    navegador.quit()

	