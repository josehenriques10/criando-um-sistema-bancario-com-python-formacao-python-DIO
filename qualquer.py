'''
Pessoal, quero fazer uma classe Contatos,

Mas quero(n sei se é realmente certo fzr isso) fazer uma classe que não 
precise ser instanciada em uma variavel a parte, para usar ela.. quero 
tipo usar ela assim ó:
'''


class Contatos:
    contatos = []

    @classmethod
    def add(cls, name):
        cls.contatos.append(name)

    @classmethod
    def add_list(cls, names):
        contatos = (names.split())

        for name in contatos:
            cls.contatos.append(name)

    @classmethod
    def get_contatos(cls):
        return cls.contatos



Contatos.add('Silvio Santos')
Contatos.add_list(
    'Pedro '
    'Jose '
    'Paulo '
    'Maria '
    'Joana '
    'César '
    'Júlio'
)
print(Contatos.get_contatos())
