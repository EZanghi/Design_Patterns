from datetime import date

class Item(object):

    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor

class Nota_fiscal(object):

    def __init__(self, razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes=''):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception('Detalhes da nota não pode ter mais do que 20 caracteres')
        self.__detalhes = detalhes
        self.__itens = itens

    #Criando as funções dentro da própria classe que serão responsáveis 
    # por chamar ações consequentes à instanciação de um novo objeto. 

        self.__envia_por_email(self)
        self.__salva_no_banco(self)
        self.__imprime(self)

    def __envia_por_email(self, nota_fiscal):
        print ('enviando nota por e-mail...')

    def __salva_no_banco(self, nota_fiscal):
        print ('salvando no banco...')        

    def __imprime(self, nota_fiscal):
        print ('imprimindo ...')

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes

##Exemplo de construtor de uma objeto com as classes Nota_fiscal e Item
## utilizando recursos da linguagem

if __name__ == '__main__':

    itens=[
        Item(
            'ITEM A',
            100
        ),
        Item(
            'ITEM B',
            200
        )
    ]

    nota_fiscal = Nota_fiscal(
        razao_social='FHSA Limitada',
        cnpj='012345678901234',
        itens=itens,
        data_de_emissao=date.today(),
        detalhes=''
    )