from abc import ABC, abstractmethod
from selenium import webdriver

class Impressora(ABC):
    def __init__(self, navegador: webdriver):
        self._navegador = navegador
        self._modelo_impressora = None
        self._host_impressora= None
        self._numero_serie_impressora = None
        self._total_impressoes_impressora = None
        self._vida_restante_toner = None
        self._total_impressoes_toner = None
        self._modelo_toner = None
        self._numero_serie_toner = None
        self._capacidade_toner = None
        self._vida_util_fusor = None
        self._vida_util_rolo_transferencia = None
        self._vida_util_bandeja_um = None
        self._vida_util_rolo_retrocesso_bandeja_um = None
        self._vida_util_bandeja_multifuncional = None
        self._vida_util_rolo_bandeja_multifuncional = None

    #Metodos da Impressora
    @property
    def modelo_impressora(self):
        if self._modelo_impressora is None:
            self._modelo_impressora = self._extrair_modelo_impressora()
        return self._modelo_impressora

    @abstractmethod
    def _extrair_modelo_impressora(self):
        pass
        
    @property
    def total_impressoes_impressora(self):
        if self._total_impressoes_impressora is None:
            self._total_impressoes_impressora = self._extrair_total_impressoes_impressora()
        return self._total_impressoes_impressora
    
    @abstractmethod
    def _extrair_total_impressoes_impressora(self):
        pass
    
    @property
    def host_impressora(self):
        if self._host_impressora is None:
            self._host_impressora = self._extrair_host_impressora()
        return self._host_impressora

    @abstractmethod
    def _extrair_host_impressora(self):
        pass

    @property
    def numero_serie_impressora(self):
        if self._numero_serie_impressora is None:
            self._numero_serie_impressora = self._extrair_numero_serie_impressora()
        return self._numero_serie_impressora
    
    @abstractmethod
    def _extrair_numero_serie_impressora(self):
        pass


    #Metodos para o Toner
    @property
    def vida_restante_toner(self):
        if self._vida_restante_toner is None:
            self._vida_restante_toner = self._extrair_vida_restante_toner()
        return self._vida_restante_toner

    @abstractmethod
    def _extrair_vida_restante_toner(self):
        pass
    
    @property
    def total_impressoes_toner(self):
        if self._total_impressoes_toner is None:
            self._total_impressoes_toner = self._extrair_total_impressoes_toner()
        return self._total_impressoes_toner

    @abstractmethod
    def _extrair_total_impressoes_toner(self):
        pass

    @property
    def modelo_toner(self):
        if self._modelo_toner is None:
            self._modelo_toner = self._extrair_modelo_toner()
        return self._modelo_toner

    @abstractmethod
    def _extrair_modelo_toner(self):
        pass

    @property
    def numero_serie_toner(self):
        if self._numero_serie_toner is None:
            self._numero_serie_toner = self._extrair_numero_serie_toner()
        return self._numero_serie_toner

    @abstractmethod
    def _extrair_numero_serie_toner(self):
        pass

    @property
    def capacidade_toner(self):
        if self._capacidade_toner is None:
            self._capacidade_toner = self._extrair_capacidade_toner()
        return self._capacidade_toner

    @abstractmethod
    def _extrair_capacidade_toner(self):
        pass


    #Outras Informações
    @property
    def vida_util_fusor(self):
        if self._vida_util_fusor is None:
            self._vida_util_fusor = self._extrair_vida_util_fusor()
        return self._vida_util_fusor

    @abstractmethod
    def _extrair_vida_util_fusor(self):
        pass

    @property
    def vida_util_rolo_transferencia(self):
        if self._vida_util_rolo_transferencia is None:
            self._vida_util_rolo_transferencia = self._extrair_vida_util_rolo_transferencia()
        return self._vida_util_rolo_transferencia

    @abstractmethod
    def _extrair_vida_util_rolo_transferencia(self):
        pass 

    @property
    def vida_util_rolo_bandeja_um(self):
        if self._vida_util_rolo_bandeja_um is None:
            self._vida_util_rolo_bandeja_um = self._extrair_vida_util_rolo_bandeja_um()
        return self._vida_util_rolo_bandeja_um

    @abstractmethod
    def _extrair_vida_util_rolo_bandeja_um(self):
        pass

    @property
    def vida_util_rolo_retrocesso_bandeja_um(self):
        if self._vida_util_rolo_retrocesso_bandeja_um is None:
            self._vida_util_rolo_retrocesso_bandeja_um = self._extrair_vida_util_rolo_retrocesso_bandeja_um()
        return self._vida_util_rolo_retrocesso_bandeja_um

    @abstractmethod
    def _extrair_vida_util_rolo_retrocesso_bandeja_um(self):
        pass

    @property
    def vida_util_bandeja_multifuncional(self):
        if self._vida_util_bandeja_multifuncional is None:
            self._vida_util_bandeja_multifuncional = self._extrair_vida_util_bandeja_multifuncional()
        return self._vida_util_bandeja_multifuncional

    @abstractmethod
    def _extrair_vida_util_bandeja_multifuncional(self):
        pass

    @property
    def vida_util_rolo_bandeja_multifuncional(self):
        if self._vida_util_rolo_bandeja_multifuncional is None:
            self._vida_util_rolo_bandeja_multifuncional = self._extrair_vida_util_rolo_bandeja_multifuncional()
        return self._vida_util_rolo_bandeja_multifuncional

    @abstractmethod
    def _extrair_vida_util_rolo_bandeja_multifuncional(self):
        pass

