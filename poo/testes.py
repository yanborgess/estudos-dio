#criando uma classe
class Bicicleta:
    #Metodos da classe 
    #Usar sempre o self.
    #init para inicar os metodos da classe
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo 
        self.ano = ano
        self.valor = valor
    #Semore deve haver o self atribuida 
    def buzinar(self):
        print('Plimplim.....')
    
    def correr(self):
        print('Vrummmmmm')

    def parar(self):
        print('Parando bicleta...')
        print('Parada!')
    #Transforma o valor dos atributos em string 
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
#Valores atribuidos a classe bicileta
b1 = Bicicleta('verde', 'caloi', 2022, 600)

#Parar poder usar os metodos da classe
b1.buzinar()
b1.correr()
b1.parar()

#Acessar os atribudos da classe
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("vermelha", "monark", 2000, 189)
print(b2)