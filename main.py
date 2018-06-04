import math as m

# BARRA = INSTANCIA DE BARRA
# TODAS AS POSICOES SAO EM RELACAO À ORIGEM
# barra.tamanho => tamanho da barra
# RELATIVO AOS APOIOS
#     barra.apoio["tipo"] => 1 - Engastamento
#                         2 - Simples e fixo
#     barra.apoio["pos_engaste"] => auto explicativo
#     barra.apoio["pos_simples"] => auto explicativo
#     barra.apoio["pos_fixo"] => auto explicativo
# RELATIVO ÀS FORCAS
#     barra.forcas["tipo"] => 1 - Pontal
#                             2 - Distribuida
#     barra.forcas["quant"] => quant de forcas

#     PARA FORCAS PONTUAIS
#     barra.forcas["pos_"+NUMERO(COMECA EM 1)] => posicao da força NUMERO
#     barra.forcas["int_"+NUMERO(COMECA EM 1)] => intensidade

#     PARA FORCAS DISTRIBUIDA
#     barra.forcas["pos_ini_"+NUMERO(COMECA EM 1)] => posicao inicial  
#     barra.forcas["pos_fim_"+NUMERO(COMECA EM 1)] => posicao final
#     barra.forcas["int_ini_"+NUMERO(COMECA EM 1)] => intensidade inicial
#     barra.forcas["int_fin_"+NUMERO(COMECA EM 1)] => intensidade final
# RELATIVO AOS MOMENTOS
#     barra.momentos["quant"] => quant de momentos
#     barra.momentos["pos_"+NUMERO(COMECA EM 1)] => posicao do momento NUMERO
#     barra.momentos["int_"+NUMERO(COMECA EM 1)] => intensidade

# PARA BARRA ANGULADA
#     angulo => angulo entre a primeira barra e o eixo horizontal
#     tamanho é baseado em lei dos cossenos


class Barra():
    def __init__(self):
        self.apoio = {}
        self.forcas = {}
        self.momentos = {}

    def set_comprimento(self):
        while True:
            alfa = float(input('Defina um comprimento (em metros 0<L<100):'))
            if alfa > 0.0 and alfa < 100.0:
                self.tamanho = alfa
                break
            else:
                print("Comprimento invalido!")

    def set_apoio(self, angulada):
        if not angulada:
            print("Defina um apoio:")
            while True:
                alfa = input("1 - Engastamento\n2- Simples e fixo\n")
                if alfa == "1":
                    while True:
                        beta = int(
                            input("Defina a posicao do engastamento:\n1 - Origem\n2 - Fim\n"))
                        if beta == 1:
                            self.apoio['pos_engaste'] = 0
                            break
                        elif beta == 2:
                            self.apoio['pos_engaste'] = self.tamanho
                            break
                    self.apoio['tipo'] = 1
                    break
                elif alfa == "2":
                    while True:
                        beta = float(
                            input("Defina a posicao do apoio simples: "))
                        if beta >= 0 and beta <= self.tamanho:
                            self.apoio["pos_simples"] = beta
                            break
                    while True:
                        beta = float(
                            input("Defina a posicao do apoio fixo: "))
                        if beta >= 0 and beta <= self.tamanho:
                            self.apoio['pos_fixo'] = beta
                            break

                    break
        else:
            while True:
                alfa = float(
                    input("Defina a distancia(0<x<100) entre os dois apoios (ambos estao no eixo horizontal): "))
                if alfa > 0 and alfa < 100:
                    self.apoio['pos_simples'] = 0
                    self.apoio['pos_fixo'] = alfa
                    break

    def set_forcas(self):
        while True:
            alfa = input(
                "Selecione um tipo de forca:\n1 - Pontual\n2 - Destribuida\n")
            if alfa == "1" or alfa == "2":
                self.forcas['tipo'] = alfa
                break
        while True:
            alfa = int(input("Digite o numero de forcas(0<x<100): "))
            if alfa >= 0 or alfa <= 100:
                self.forcas['quant'] = alfa
                break

        if self.forcas['tipo'] == "1":
            print("Digite a posicao da forca(em metros)\ne depois a intensidade(em Kn)\n")
            for alfa in range(1, self.forcas['quant']+1):
                print("Forca "+str(alfa))
                while True:
                    beta = float(input("Digite a pos da forca: "))
                    if beta >= 0 and beta <= self.tamanho:
                        self.forcas['pos_'+str(alfa)] = beta
                        break
                while True:
                    beta = float(input("Digite a intensidade da forca: "))
                    if beta >= -10e6 and beta <= 10e6:
                        self.forcas['int_'+str(alfa)] = beta
                        break
        elif self.forcas['tipo'] == "2":
            for alfa in range(1, self.forcas['quant']+1):
                print("Forca "+str(alfa))
                while True:
                    beta = float(input("Digite a pos inicial da forca: "))
                    if beta >= 0 and beta <= self.tamanho:
                        self.forcas['pos_ini_'+str(alfa)] = beta
                        break
                while True:
                    beta = float(input("Digite a pos final da forca: "))
                    if beta >= 0 and beta <= self.tamanho:
                        self.forcas['pos_fin_'+str(alfa)] = beta
                        break
                while True:
                    beta = float(
                        input("Digite a intensidade inicial da forca: "))
                    if beta >= -10e6 and beta <= 10e6:
                        self.forcas['int_ini_'+str(alfa)] = beta
                        break
                while True:
                    beta = float(
                        input("Digite a intensidade final da forca: "))
                    if beta >= -10e6 and beta <= 10e6:
                        self.forcas['int_fin_'+str(alfa)] = beta
                        break

    def set_momentos(self):
        while True:
            alfa = int(input("Digite o numero de momentos(0<=x<=100): "))
            if alfa >= 0 or alfa <= 100:
                self.momentos['quant'] = alfa
                break
        for alfa in range(1, self.momentos['quant']+1):
            print("Momento "+str(alfa))
            while True:
                beta = float(
                    input("Digite posicao do momento: "))
                if beta >= 0 and beta <= self.tamanho:
                    self.momentos['pos_'+str(alfa)] = beta
                    break
            while True:
                beta = float(
                    input("Digite intensidade do momento: "))
                if beta >= -10e6 and beta <= 10e6:
                    self.momentos['int_'+str(alfa)] = beta
                    break


def BarraSimples():
    barraSimples = Barra()
    barraSimples.set_comprimento()
    barraSimples.set_apoio(0)
    barraSimples.set_forcas()
    barraSimples.set_momento()


def BarraAngulada():
    while True:
        angulo = float(
            input("Digite o angulo(graus) entre a primeira barra e o eixo X (0<x<180): "))
        if angulo > 0 and angulo < 180:
            break
    barra_princ = Barra()
    barra_secun = Barra()
    barra_princ.set_apoio(1)
    print("BARRA NA ORIGEM")
    barra_princ.set_comprimento()
    tamanho_barra_secundaria = m.sqrt(m.pow(barra_princ.tamanho, 2)+m.pow(barra_princ.apoio['pos_fixo'], 2)-2*barra_princ.tamanho*barra_princ.apoio['pos_fixo']*m.cos(m.radians(angulo)))
    print("O tamanho da segunda barra será "+str(tamanho_barra_secundaria))
    barra_secun.tamanho = tamanho_barra_secundaria
    barra_princ.set_forcas()
    barra_princ.set_momentos()
    barra_princ.set_forcas()
    barra_princ.set_momentos()
    print("SEGUNDA BARRA")
    barra_secun.set_forcas()
    barra_secun.set_momentos()

print("Bem vindo à calculadora de esforcos do Grupo Rabello Viado!\nIntegrantes:\nEugenio Sabatini\nGabriel dos Anjos\nPedro Rabello\nVitor Duque\n\n")
while True:
    alfa = int(
        input("Escolha um tipo de barra:\n1-Simples\n2-Angulada\n"))
    if alfa == 1:
        BarraSimples()
        break
    elif alfa == 2:
        BarraAngulada()
        break

