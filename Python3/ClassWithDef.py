class Cat:
    def __init__(self, nome, qtd):
        self.__nome = nome
        self.__qtd = qtd

    def __str__(self):
        return 'Cat{\n nome='+self__nome+',\n idade='+str(self.__qtd)'