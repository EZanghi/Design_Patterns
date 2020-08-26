from nota_fiscal import Nota_fiscal, Item

class Criador_de_nota_fiscal(object):

    def __init__(self):

        self.__razao_social = None
        self.__cnpj = None
        self.__data_de_emissao = None
        self.__detalhes = ''
        self.__itens = None

    def com_razao_social(self, razao_social):
        self.__razao_social = razao_social
        return self

    def com_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def com_data_de_emissao(self, data_de_emissao):
        self.__data_de_emissao = data_de_emissao
        return self

    def com_itens(self, itens):
        self.__itens = itens
        return self

    def constroi(self):
        if self.__razao_social is None:
            raise Exception('Razão social deve ser preenchida')
        if self.__cnpj is None:
            raise Exception('CNPJ deve ser preenchido')
        if self.__itens is None:
            raise Exception('Itens deve ser preenchido')

        return Nota_fiscal(
            razao_social=self.__razao_social, 
            cnpj=self.__cnpj, 
            itens=self.__itens, 
            data_de_emissao=self.__data_de_emissao, 
            detalhes = self.__detalhes
        )

if __name__ == '__main__':

    itens=[
        Item(
            descricao='ITEM A',
            valor=100
        ),
        Item(
            descricao='ITEM B',
            valor=200
        )
    ]


    # usando nosso Builder.
    nota_fiscal = (Criador_de_nota_fiscal()
        .com_razao_social('FHSA Limitada')
        .com_cnpj('012345678901234')
        .com_itens(itens)
        .constroi())

    print (nota_fiscal.razao_social)
    print (nota_fiscal.cnpj)
    print (nota_fiscal.detalhes)