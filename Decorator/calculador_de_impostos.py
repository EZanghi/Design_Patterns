from impostos import ISS, ICMS, PIS, COFINS

class Calculador_de_Impostos(object):

    def realiza_calculo(self, orcamento, imposto):

        imposto_calculado = imposto.calcula(orcamento)

        print(imposto_calculado)

if __name__ == '__main__':

    from orcamento import Orcamento, Item

    calculador = Calculador_de_Impostos()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 100))
    orcamento.adiciona_item(Item('ITEM - 2', 50))
    orcamento.adiciona_item(Item('ITEM - 3', 400))

    print('ISS e ICMS')
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

    print('ISS com ICMS')
    calculador.realiza_calculo(orcamento, ISS(ICMS()))

    print('PIS e COFINS')
    calculador.realiza_calculo(orcamento, PIS())
    calculador.realiza_calculo(orcamento, COFINS())

    print('PIS com COFINS')
    calculador.realiza_calculo(orcamento, PIS(COFINS()))