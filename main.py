from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from time import sleep
from impressoras import Impressora4070, Impressora4080, Impressora4020
from pdfconfig import criar_pdf_impressora
import json

diretorio_pdf = "pdfs/"

options = Options()
options.add_argument("--headless")
options.add_argument('-width=1600')
options.add_argument('-height=900')

# Configuração inicial do navegador
navegador = webdriver.Firefox(options=options)

#Abrindo arquivo json que contem os Ips de todas as impressoras
with open('ipimpressoras.json', 'r') as arquivo_json:
    ips_impressoras = json.load(arquivo_json)


try:
    for ip in ips_impressoras["IP das Impressoras ELCMAR"]:
        impressora = None
        navegador.get(f"http://{ip}/sws/index.html")
        sleep(3)

        try:
            # Tenta identificar a Impressora4070
            navegador.find_element(By.XPATH, "//span[text()='SL-M4070FR']")
            impressora = Impressora4070(navegador)
            impressora.montar_impressora()
        except NoSuchElementException:
            pass  # Se não encontrar, prossegue para a próxima tentativa

        try:
            # Tenta identificar a Impressora4080 se a 4070 não foi identificada
            if not impressora:
                navegador.find_element(By.NAME, "ruifw_StatusFrm")
                impressora = Impressora4080(navegador)
                impressora.montar_impressora()
        except NoSuchElementException:
            pass

        try:
            # Tenta identificar a Impressora4020 se a 4070 e 4080 não foram identificadas
            if not impressora:
                navegador.find_element(By.XPATH, "//span[text()='SL-M4020ND']")
                impressora = Impressora4020(navegador)
                impressora.montar_impressora()
        except NoSuchElementException:
            pass

        if not impressora:
            raise NoSuchElementException("Não foi encontrado o modelo de Impressora Informado")

        criar_pdf_impressora(impressora, nome_arquivo=f"{diretorio_pdf}informacoes_impressora_{impressora.host}_{impressora.modelo}.pdf")

    #Garante que a próxima pagina carrega não terá interferencia das anteriores
    navegador.delete_all_cookies()


except TimeoutException as e:
    print(f"Erro: {e}")
    raise TimeoutException("A operação demorou muito para ser concluída e foi interrompida.")


finally:
    navegador.quit()

	