class Pessoa:
    def __init__(self, nome, peso, idade, alimento="", comendo=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.alimento = alimento

    def comer(self):
        if self.comendo:
            print(f"{self.nome} já está comendo.")
            return
        self.comendo = True
        print(f"{self.nome} está comendo {self.alimento}.")

    def pararomer(self):
        if self.comendo:
            print(f"{self.nome} não está comendo.")
            return
        self.comendo = False
        print(f"{self.nome} parou de comer.")
    def dormir(self):
        if self.comendo:
            print(f"{self.nome} não pode dormir enquanto come!")
            return
        print(f"{self.nome} está indo dormir.")

    def parardormir(self):
        print(f"{self.nome} acordou!")

class Conta:
    def __init__(self,numeroconta,nomecliente,tipoconta,limite=0.0, saldo=0.0, status=True):
        self.numeroconta = numeroconta
        self.nomecliente = nomecliente
        self.tipoconta = tipoconta
        self.saldo = saldo
        self.status = status
        self.limite = limite

    def ativarconta(self):
        if self.status:
            print("Sua conta esta ativa!")
        else:
            self.status = True
            print("Conta ativada com sucesso!")
    def depositar(self, valor):
        if not self.status:
            print("Não é possivel depositar, conta inativa!")
            return
        if valor > 0:
            self.saldo += valor
            print (f"Deposito de R${valor:.2f} realizado.")
        else:
            print ("Valor inavlido")

    def sacar(self, valor):
        if not self.status:
            print("Saque indisponível, conta inativa!")
            return
        if 0 < valor <= self.saldo + self.limite:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def verificarsaldo(self):
            print(f"Saldo atual da conta {self.numeroconta}: R${self.saldo:.2f}")
            return self.saldo

class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def comer(self ):
        print (f"o {self.nome} foi comer...")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)

    def miar(self):
        print (f"O {self.nome} esta miando...")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)

    def latir(self):
        print (f"O {self.nome} esta latindo...")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)

    def mugir(self):
        print (f"O {self.nome} esta mugindo...")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)

    def guinchar(self):
        print (f"O {self.nome} esta guinchando...")

class Ingresso:
    def __init__(self,valor):
        self.valor = valor
    def valor(self):
        print (f"O ingresso é R${self.valor} reais")

class Vip(Ingresso):
    def __init__(self,valor):
        super().__init__(valor)
        self.valor *=1.5
    def valor(self):
        print (f"O ingresso vip é R$ {self.valor} reais.")

class Forma:
    def __init__(self, area, perimetro):
        self.area = area
        self.perimetro = perimetro

class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        area = self.calcular_area()
        perimetro = self.calcular_perimetro()
        super().__init__(area, perimetro)

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

    def exibir_dados(self):
        print(f"A área do retângulo é: {self.area}")
        print(f"O perímetro do retângulo é: {self.perimetro}")


class Atleta:
    def __init__(self, aposentado, peso):
        self.aposentado = aposentado
        self.peso = peso
        self.aquecido = False

    def aquecer(self):
        if not self.aposentado:
            self.aquecido = True
            print("Atleta está aquecido.")
        else:
            print("Atleta aposentado não pode aquecer.")

    def aposentar(self):
        self.aposentado = True
        print("Atleta foi aposentado.")

class Corredor(Atleta):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)

    def aquecer(self):
        if not self.aposentado:
            self.aquecido = True
            print("Corredor está aquecido.")
        else:
            print("Corredor aposentado não pode aquecer.")

    def aposentar(self):
        self.aposentado = True
        print("Corredor foi aposentado.")

class Nadador (Atleta):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)

    def aquecer(self):
        if not self.aposentado:
            self.aquecido = True
            print("Nadador está aquecido.")
        else:
            print("Nadador aposentado não pode aquecer.")

    def aposentar(self):
        self.aposentado = True
        print("Nadador foi aposentado.")

class Ciclista(Atleta):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)

    def aquecer(self):
        if not self.aposentado:
            self.aquecido = True
            print("O ciclista está aquecido.")
        else:
            print("Ciclista aposentado não pode aquecer.")

    def aposentar(self):
        self.aposentado = True
        print("Ciclista foi aposentado.")
"""falta o triatleta
"""
    """import datetime

agora = datetime.datetime.now()

print("Data e hora atual:", agora)
print("Ano:", agora.year)
print("Mês:", agora.month)
print("Dia:", agora.day)
print("Hora:", agora.hour)
print("Minuto:", agora.minute)
print("Segundo:", agora.second)
print("Dia da semana:", agora.strftime("%A"))"""


"""class animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f' O {self.nome} foi comer...')
 class Gato(Animal):
    def __init__(self, nome, cor):
 super().__init__(nome, cor)
 def miar(self):
        print( f' O {self.nome} foi miando...')"""
