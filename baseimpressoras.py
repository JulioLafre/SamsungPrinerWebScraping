from abc import ABC, abstractmethod
from selenium import webdriver

class Impressora(ABC):
    def __init__(self, navegador: webdriver):
        self._navegador = navegador
        self._modelo = None
        self._host= None
        self._numero_serie = None
        self._total_impressoes = None
        self._vida_restante_toner = None
        self._total_impressoes_toner = None
        self._modelo_toner = None
        self._numero_serie_toner = None
        self._capacidade_toner = None
        self._vida_util_fusor = None
        self._vida_util_rolo_transferencia = None
        self._vida_util_rolo_bandeja_um = None
        self._vida_util_rolo_retrocesso_bandeja_um = None
        self._vida_util_bandeja_multifuncional = None
        self._vida_util_rolo_bandeja_multifuncional = None

    #Metodos da Impressora
    @property
    def modelo(self):
        if self._modelo is None:
            self._modelo = self._extrair_modelo()
        return self._modelo

    @abstractmethod
    def _extrair_modelo(self):
        pass
        
    @property
    def total_impressoes(self):
        if self._total_impressoes is None:
            self._total_impressoes = self._extrair_total_impressoes()
        return self._total_impressoes
    
    @abstractmethod
    def _extrair_total_impressoes(self):
        pass
    
    @property
    def host(self):
        if self._host is None:
            self._host = self._extrair_host()
        return self._host

    @abstractmethod
    def _extrair_host(self):
        pass

    @property
    def numero_serie(self):
        if self._numero_serie is None:
            self._numero_serie = self._extrair_numero_serie()
        return self._numero_serie
    
    @abstractmethod
    def _extrair_numero_serie(self):
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

