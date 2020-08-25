'''
Exemplo de aplicação do padrão Decorator => O Decorator é para compor e dividir comportamento em fatias onde cada fatia (objeto) representa uma parte da responsabilidade.

Quando compomos comportamento, através de classes que recebem objetos do mesmo tipo que elas mesmas 
(nesse caso, ISS que é um Imposto, recebe em seu construtor outro Imposto) para fazerem parte de seu comportamento, 
de uma maneira que seu uso é definido a partir do que se passou para a instanciação dos objetos, 
é o que caracteriza o Design Pattern chamado Decorator.

O Python oferece ainda uma implementação nativa que pode ser vista abaixo do "def IPVX" que em seguida é chamado "@IPVX" sobre 
o método ou função desejado.
No design pattern (criando uma classe que recebe objetos do mesmo tipo...) podemos optar em chamar ou não o comportamento durante sua execução
utilizando o decorator da linguagem ele sempre será utilizado, portanto cabe avaliar a real necessidade.
'''

from abc import ABCMeta, abstractmethod

class Imposto(object):
    __metaclass__ = ABCMeta

    def __init__(self,outro_imposto = None):
        self.__outro_imposto = outro_imposto

    def calculo_do_outro_imposto(self, orcamento):

        if self.__outro_imposto is None:
            return 0
        else:
            return self.__outro_imposto.calcula(orcamento)

    @abstractmethod
    def calcula(self, orcamento):
        pass

class Template_de_imposto_condicional(Imposto):

    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento) + self.calculo_do_outro_imposto(orcamento)
        else:
            return self.minima_taxacao(orcamento) + self.calculo_do_outro_imposto(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass

def IPVX(metodo_ou_funcao): #recurso da linguagem que permite "decorar" funções ou métodos; para isso faz-se a implmentação em seguida o chama sobre a função/método desejado com "@nome_da_função"
        
        def wrapper(self, orcamento): #esta função serve para "empacotar" a função/método recebido como parâmetro
        return metodo_ou_funcao(self, orcamento) + 50.0
    return wrapper

class ISS(Imposto):

    def calcula(self, orcamento):
        return orcamento.valor * 0.1 + self.calculo_do_outro_imposto(orcamento)

class ICMS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06 + self.calculo_do_outro_imposto(orcamento)

class PIS(Template_de_imposto_condicional):

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05

class COFINS(Template_de_imposto_condicional):

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06

    def __tem_item_maior_que_100_reais(self, orcamento):

        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False
