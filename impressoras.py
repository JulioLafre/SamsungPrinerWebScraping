from baseimpressoras import Impressora
from selenium.webdriver.common.by import By
from time import sleep

class Impressora4070(Impressora):
    def __init__(self, navegador):
        super().__init__(navegador)


    #Metodos para Navegar na Página
    def abrir_aba_informacoes(self):
        botao_informacao = self._navegador.find_element(By.XPATH, "//button[text()='Informacao']")
        botao_informacao.click()

    def abrir_aba_suprimentos(self):
        botao_suprimentos = self._navegador.find_element(By.XPATH, "//span[contains(text(),'Suprimentos')]/ancestor::a[1]")
        botao_suprimentos.click()

    def abrir_aba_contadores_uso(self):
        botao_contadores_uso = self._navegador.find_element(By.XPATH, "//span[contains(text(),'Contadores de uso')]/ancestor::a[1]")
        botao_contadores_uso.click()


    #Metodos Obrigatórios
    def _extrair_modelo(self):
        return self._navegador.find_element(By.XPATH, "//div[text()='Nome do modelo']/following-sibling::div[1]").text

    def _extrair_host(self):
        return self._navegador.find_element(By.XPATH, "//div[text()='Nome do host']/following-sibling::div[1]").text

    def _extrair_numero_serie(self):
        return self._navegador.find_element(By.XPATH, "//div[text()='Número de série']/following-sibling::div[1]").text

    def _extrair_total_impressoes(self):
        return self._navegador.find_element(By.XPATH, "//div[contains(text(),'Total de impressões')]/ancestor::td/following-sibling::td[last()]//div").text

    def _extrair_vida_restante_toner(self):
        return self._navegador.find_element(By.XPATH, "//label[contains(text(),'Restante:')]/following-sibling::div[1]").text

    def _extrair_total_impressoes_toner(self):
        return self._navegador.find_element(By.XPATH, "//label[contains(text(),'Impressão:')]/following-sibling::div[1]").text

    def _extrair_modelo_toner(self):
        return self._navegador.find_element(By.XPATH, "//label[contains(text(),'ID modelo:')]/following-sibling::div[1]").text

    def _extrair_numero_serie_toner(self):
        return self._navegador.find_element(By.XPATH, "//label[contains(text(),'Número de série:')]/following-sibling::div[1]").text 

    def _extrair_capacidade_toner(self):
        return self._navegador.find_element(By.XPATH, "//label[contains(text(),'Capacidade')]/following-sibling::div[1]").text

    def _extrair_vida_util_fusor(self):
        return self._navegador.find_element(By.XPATH, "//label[contains(text(),'Vida útil do fusor:')]/following-sibling::div[1]").text

    def _extrair_vida_util_rolo_transferencia(self):
        return self._navegador.find_element(By.XPATH, "//label[contains(text(),'Vida útil do rolo de transferência:')]/following-sibling::div[1]").text

    def _extrair_vida_util_rolo_bandeja_um(self):
        return self._navegador.find_element(By.XPATH, "//label[contains(text(),'Vida útil do rolo da bandeja 1:')]/following-sibling::div[1]").text

    def _extrair_vida_util_rolo_retrocesso_bandeja_um(self):
        return self._navegador.find_element(By.XPATH, "//label[contains(text(),'Bandeja 1 Vida útil do rolo de retrocesso:')]/following-sibling::div[1]").text

    def _extrair_vida_util_bandeja_multifuncional(self):
        return self._navegador.find_element(By.XPATH, "//label[contains(text(),'Vida útil do rolo da bandeja multifuncional:')]/following-sibling::div[1]").text

    def _extrair_vida_util_rolo_bandeja_multifuncional(self):
        return self._navegador.find_element(By.XPATH, "//label[contains(text(),'Bandeja multifuncional Vida útil do rolo de retrocesso:')]/following-sibling::div[1]").text

    #Metodo de extração de informalçoes
    def montar_impressora(self):
        _ = self.modelo
        _ = self.host
        _ = self.numero_serie
        self.abrir_aba_informacoes()
        sleep(3)
        self.abrir_aba_suprimentos()
        sleep(5)
        _ = self.vida_restante_toner
        _ = self.total_impressoes_toner
        _ = self.modelo_toner
        _ = self.numero_serie_toner
        _ = self.capacidade_toner
        _ = self.vida_util_fusor
        _ = self.vida_util_rolo_transferencia
        _ = self.vida_util_rolo_bandeja_um
        _ = self.vida_util_rolo_retrocesso_bandeja_um
        _ = self.vida_util_bandeja_multifuncional
        _ = self.vida_util_rolo_bandeja_multifuncional
        self.abrir_aba_contadores_uso()
        sleep(5)
        _ = self.total_impressoes


#Como a pagina da 4070 e da 4020 são iguais, não a problema de herdar os mesmos metodos, caso venha a mudar algo na pagina, implemente as mudanças na classe abaixo
class Impressora4020(Impressora4070):
    def __init__(self, navegador):
        super().__init__(navegador)


class Impressora4080(Impressora):
    def __init__(self, navegador):
        super().__init__(navegador)

    #Metodos de Navegação na Página
    def abrir_aba_informacoes(self):
        botao_informacao = self._navegador.find_element(By.ID, "sws_topMenuName_Information")
        botao_informacao.click()
        self._navegador.switch_to.default_content()

    def abrir_aba_suprimentos(self):
        self._navegador.switch_to.frame("ruifw_LeftFrm")
        botao_suprimentos = self._navegador.find_element(By.XPATH, "//td[text()='Suprimentos']")
        botao_suprimentos.click()
        self._navegador.switch_to.default_content()

    def abrir_aba_contadores_uso(self):
        self._navegador.switch_to.frame("ruifw_LeftFrm")
        botao_contadores_uso = self._navegador.find_element(By.XPATH, "//td[text()='Conts uso']")
        botao_contadores_uso.click()
        self._navegador.switch_to.default_content()


    #Metodos Obrigatórios
    def _extrair_modelo(self):
        self._navegador.switch_to.frame('ruifw_MainFrm')
        texto_modelo = self._navegador.find_element(By.XPATH, "//td[text()='Nome do modelo']/following-sibling::td[1]").text
        self._navegador.switch_to.default_content()
        return texto_modelo

    def _extrair_host(self):
        self._navegador.switch_to.frame('ruifw_MainFrm')
        texto_host = self._navegador.find_element(By.XPATH, "//td[text()='Nome do Dispositivo']/following-sibling::td[1]").text
        self._navegador.switch_to.default_content()
        return texto_host

    def _extrair_numero_serie(self):
        self._navegador.switch_to.frame('ruifw_MainFrm')
        texto_numero_serie = self._navegador.find_element(By.XPATH, "//td[text()='Número de série']/following-sibling::td[1]").text
        self._navegador.switch_to.default_content()
        return texto_numero_serie

    def _extrair_total_impressoes(self):
        self._navegador.switch_to.frame('ruifw_MainFrm')
        texto_total_impressoes = self._navegador.find_element(By.XPATH,"//tr[@id='swstable_counterTotalList_expandTR_2']/td[last()]").text
        self._navegador.switch_to.default_content()
        return texto_total_impressoes

    def _extrair_vida_restante_toner(self):
        self._navegador.switch_to.frame('ruifw_MainFrm')
        texto_vida_restante_toner = self._navegador.find_element(By.ID, "remainCont").text
        self._navegador.switch_to.default_content()
        return texto_vida_restante_toner

    def _extrair_total_impressoes_toner(self):
        self._navegador.switch_to.frame('ruifw_MainFrm')
        texto_total_impressoes_toner = self._navegador.find_element(By.ID, "pageCont").text
        self._navegador.switch_to.default_content()
        return texto_total_impressoes_toner

    def _extrair_modelo_toner(self):
        self._navegador.switch_to.frame('ruifw_MainFrm')
        texto_modelo_toner = self._navegador.find_element(By.ID, "remainCont").text
        self._navegador.switch_to.default_content()
        return texto_modelo_toner

    def _extrair_numero_serie_toner(self):
        self._navegador.switch_to.frame('ruifw_MainFrm')
        texto_numero_serie_toner = self._navegador.find_element(By.ID, "cartCont").text
        self._navegador.switch_to.default_content()
        return texto_numero_serie_toner

    def _extrair_capacidade_toner(self):
        self._navegador.switch_to.frame('ruifw_MainFrm')
        texto_capacidade_toner = self._navegador.find_element(By.ID, "capacityCont").text
        self._navegador.switch_to.default_content()
        return texto_capacidade_toner

    def _extrair_vida_util_fusor(self):
        self._navegador.switch_to.frame('ruifw_MainFrm')
        texto_vida_util_fusor = self._navegador.find_element(By.ID, "fuserAssemblyRemaining").text
        self._navegador.switch_to.default_content()
        return texto_vida_util_fusor

    def _extrair_vida_util_rolo_transferencia(self):
        self._navegador.switch_to.frame('ruifw_MainFrm')
        texto_vida_util_rolo_tranferencia = self._navegador.find_element(By.ID, "t2RollerLife").text
        self._navegador.switch_to.default_content()
        return texto_vida_util_rolo_tranferencia

    def _extrair_vida_util_rolo_bandeja_um(self):
        self._navegador.switch_to.frame('ruifw_MainFrm')
        texto_vida_util_rolo_bandeja_um = self._navegador.find_element(By.ID, "tray1RollerLife").text
        self._navegador.switch_to.default_content()
        return texto_vida_util_rolo_bandeja_um

    def _extrair_vida_util_rolo_retrocesso_bandeja_um(self):
        self._navegador.switch_to.frame('ruifw_MainFrm')
        texto_vida_util_rolo_retrocesso_bandeja_um = self._navegador.find_element(By.ID, "tray1RtdRollerLife").text
        self._navegador.switch_to.default_content()
        return texto_vida_util_rolo_retrocesso_bandeja_um

    def _extrair_vida_util_bandeja_multifuncional(self):
        self._navegador.switch_to.frame('ruifw_MainFrm')
        texto_vida_util_badeja_multifuncional = self._navegador.find_element(By.ID, "mpTrayRollerLife").text
        self._navegador.switch_to.default_content()
        return texto_vida_util_badeja_multifuncional
        
    def _extrair_vida_util_rolo_bandeja_multifuncional(self):
        self._navegador.switch_to.frame('ruifw_MainFrm')
        texto_vida_util_rolo_bandeja_multifuncional = self._navegador.find_element(By.ID, "aDFRollerLife").text
        self._navegador.switch_to.default_content()
        return texto_vida_util_rolo_bandeja_multifuncional

    #Metodo de extração de informalçoes
    def montar_impressora(self):
        _ = self.modelo
        _ = self.host
        _ = self.numero_serie
        self.abrir_aba_informacoes()
        sleep(3)
        self.abrir_aba_suprimentos()
        sleep(5)
        _ = self.vida_restante_toner
        _ = self.total_impressoes_toner
        _ = self.modelo_toner
        _ = self.numero_serie_toner
        _ = self.capacidade_toner
        _ = self.vida_util_fusor
        _ = self.vida_util_rolo_transferencia
        _ = self.vida_util_rolo_bandeja_um
        _ = self.vida_util_rolo_retrocesso_bandeja_um
        _ = self.vida_util_bandeja_multifuncional
        _ = self.vida_util_rolo_bandeja_multifuncional
        self.abrir_aba_contadores_uso()
        sleep(5)
        _ = self.total_impressoes
