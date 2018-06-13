import math as m
import numpy as np
import matplotlib.pyplot as plt

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
        self.apoio = []
        self.forcas = []
        self.momentos = []
        self.inclinacao = 0
        self.tamanho = 0

    def set_comprimento(self):
        while True:
            alfa = float(input('Defina um comprimento (em metros 0<=L<=100): '))
            if alfa > 0.0 and alfa <= 100.0:
                self.tamanho = alfa
                break
            else:
                print("Comprimento invalido!")
    def set_inclinacao(self):
        while True:
            alfa = float(input('Defina um inclinacao (em graus 0º<=α<90º): '))
            if alfa>= 0.0 and alfa <= 90.0:
                self.inclinacao = alfa
                break
            else:
                print('Inclinação inválida')
    def set_apoio(self):
        print("Defina um apoio: ")
        while True:
            alfa = input("1 - Engastamento\n2- Simples e fixo\n")
            if alfa == "1":
                while True:
                    beta = int(input("Defina a posicao do engastamento:\n1 - Origem\n2 - Fim\n"))
                    if beta == 1:
                        self.apoio.append(engaste(0,self.inclinacao))
                        break
                    elif beta == 2:
                        self.apoio.append(engaste(self.tamanho,self.inclinacao))
                        break
                break
            elif alfa == "2":
                apoioS = apoioSimples()
                apoioS.set_posicao(self.tamanho,self.inclinacao)
                self.apoio.append(apoioS)
                apoioF = apoioFixo()
                apoioF.set_posicao(self.tamanho,self.inclinacao)
                self.apoio.append(apoioF)
                break

    def set_forcas(self):
        while True:
            alfa = int(input("Digite o numero de forcas(0<x<100): "))
            if alfa >= 0 or alfa <= 100:
                break
            else:
                print('Número inválido')
        for i in range(0, alfa):
            print('Força número %d' %(i+1))
            f = forca()
            f.set_intensidade()
            f.set_posicao(self.tamanho,self.inclinacao)
            f.set_angulo()
            self.forcas.append(f)
            
    def set_momentos(self):
        while True:
            alfa = int(input("Digite o numero de momentos(0<=x<=100): "))
            if alfa >= 0 or alfa <= 100:
                break
            else:
                print('Número inválido')
        for i in range(0, alfa):
            print('Momento número %d' %(i+1))
            m = momento()
            m.set_intensidade()
            self.momentos.append(m)
            
        
class engaste():
    def __init__(self,pos,inclinacao):
        self.reacaoX = 0
        self.reacaoY = 0
        self.reacaoM = 0
        self.posicaoX = pos*m.cos(m.radians(inclinacao))
        self.posicaoY = pos*m.sin(m.radians(inclinacao))

    
    
class apoioFixo():
    def __init__(self):
        self.reacaoX = 0
        self.reacaoY = 0
        self.posicaoX = 0
        self.posicaoY = 0

    def set_posicao(self,tamanho,inclinacao):
        while True:
            alfa = float(input('Digite a posição na barra do apoio fixo, que deve ser dentro dos limites da barra: '))
            if alfa >= 0.0 and alfa <= tamanho:
                self.posicaoX = m.cos(m.radians(inclinacao))*alfa
                self.posicaoY = m.sin(m.radians(inclinacao)) * alfa
                break
            else:
                print('Posição inválida')

class apoioSimples():
    def __init__(self):
        self.reacaoY = 0
        self.posicaoX = 0
        self.posicaoY = 0

    def set_posicao(self,tamanho,inclinacao):
        while True:
            alfa = float(input('Digite a posição na barra do apoio simples, que deve ser dentro dos limites da barra: '))
            if alfa >= 0.0 and alfa <= tamanho:
                self.posicaoX = m.cos(m.radians(inclinacao))*alfa
                self.posicaoY = m.sin(m.radians(inclinacao)) * alfa
                break
            else:
                print('Posição inválida')


class forca():
    def __init__(self):
        self.intensidade = 0
        self.posicaoX = 0
        self.posicaoY = 0
        self.angulo = 0

    def set_intensidade(self):
        while True:
            alfa = float(input('Digite a intensidade (-1000000<=I<=1000000): '))
            if alfa >= -1000000.0 and alfa <= 1000000.0:
                self.intensidade = alfa
                break
            else:
                print('Intensidade inválida')

    def set_posicao(self,tamanho,inclinacao):
        while True:
            alfa = float(input('Digite a posição na barra da força, que deve ser dentro dos limites da barra: '))
            if alfa >= 0.0 and alfa <= tamanho:
                self.posicaoX = m.cos(m.radians(inclinacao))*alfa
                self.posicaoY = m.sin(m.radians(inclinacao)) * alfa
                break
            else:
                print('Posição inválida')

    def set_angulo(self):
        while True:
            alfa = float(input('Digite o ângulo de aplicação da força (0º<=β<=180º): '))
            if alfa >= 0.0 and alfa <= 180.0:
                self.angulo = alfa
                break
            else:
                print('Ângulo de aplicação inválido')
        self.FX = self.intensidade * m.cos(m.radians(self.angulo))
        self.FY = self.intensidade * m.sin(m.radians(self.angulo))

class momento():
    def __init__(self):
        self.intensidade = 0

    def set_intensidade(self):
        while True:
            alfa = float(input('Digite a intensidade (-1000000<=I<=1000000): '))
            if alfa >= -1000000.0 and alfa <= 1000000.0:
                self.intensidade = alfa
                break
            else:
                print('Intensidade inválida')



print("Bem vindo à calculadora de esforcos do Grupo 19!\nIntegrantes:\nEugenio Sabatini\nGabriel dos Anjos\nVitor Duque\nPedro Rabelo Chato\n")
barra = Barra()
barra.set_comprimento()
barra.set_inclinacao()
barra.set_apoio()
barra.set_forcas()
barra.set_momentos()
if len(barra.apoio) == 1:
    plt.plot([0,barra.tamanho*m.cos(m.radians(barra.inclinacao))],[0,barra.tamanho*m.sin(m.radians(barra.inclinacao))],[barra.apoio[0].posicaoX],[barra.apoio[0].posicaoY],'ro',)
else:
    plt.plot([0,barra.tamanho*m.cos(m.radians(barra.inclinacao))],[0,barra.tamanho*m.sin(m.radians(barra.inclinacao))],[barra.apoio[0].posicaoX],[barra.apoio[0].posicaoY],'b^',[barra.apoio[1].posicaoX],[barra.apoio[1].posicaoY],'r^',)
plt.show()
sumFX = 0
sumFY = 0
passa = input('Então vamos lá: para começar a resolução digite qualquer coisa...')
print()
print('Primeiramente vamos calcular as componentes das forças em cada direção, sendo:\nFX = intensidade * cos(ângulo de aplicação)\nFY = intensidade* sen(ângulo de aplicação)')
for i in range(0, len(barra.forcas)): #somatoria das forcas dadas (x e y)
    print('Força %d' %(i+1))
    print('\t FX = %dN' %barra.forcas[i].FX)
    print('\t FY = %dN' %barra.forcas[i].FY)
    sumFX += barra.forcas[i].FX
    sumFY += barra.forcas[i].FY
print()
print('Agora podemos calcular a resultante em cada direção')
print('FX = %dN' %sumFX)
print('FY = %dN' %sumFY)
print()
passar = input('Agora vamos para os momentos das forças! Para continuar digite qualquer coisa...')
print()
print('Como o problema só tem duas dimensões todos os momentos serão na direção z. Assim a resultante dos momentos aplicados é a somente a soma das intesidades')
sumM = 0
for i in range(0, len(barra.momentos)): #somatoria dos momentos dados
    sumM += barra.momentos[i].intensidade
print('Momento total é M = %d' %sumM)
print()
if len(barra.apoio) == 1:
    barra.apoio[0].reacaoX, barra.apoio[0].reacaoY = -sumFX, -sumFY
    M = 0
    print('O momento de cada força em relação a uma referência é o produto vetorial da distância entre do ponto de aplicação e a referência e o vetor força. Como referência adotaremos o engastamento')
    print()
    for i in range(0, len(barra.forcas)): #soma dos momentos provocados pelas forças
        print('Momento da Força %d:' %(i+1))
        print('\t M = %dN.m' %((barra.forcas[i].posicaoX - barra.apoio[0].posicaoX)*barra.forcas[i].FY - (barra.forcas[i].posicaoY - barra.apoio[0].posicaoY)*barra.forcas[i].FX))
        M += (barra.forcas[i].posicaoX - barra.apoio[0].posicaoX)*barra.forcas[i].FY - (barra.forcas[i].posicaoY - barra.apoio[0].posicaoY)*barra.forcas[i].FX
    print()
    print('A soma é Mforças = %dN.m' %M)
    barra.apoio[0].reacaoM = -(sumM + M)
    print()
    passar = input('Agora montaremos as equações! Digite qualquer coisa para continuar...')
    print()
    print('Nós podemos dizer que:\nXengastamento = -FX\nYengastamento = -FY\nMengastamento = -(Mtotal + Mforças)')
    print()
    passar = input('Para ver a resposta digite qualquer coisa...')
    print()
    print('Reação X do engastamento: %dN' %barra.apoio[0].reacaoX)
    print('Reação Y do engastamento: %dN' %barra.apoio[0].reacaoY)
    print('Reação de momento do engastamento: %dN.m' %barra.apoio[0].reacaoM)

else:
    M = 0
    print('O momento de cada força em relação a uma referência é o produto vetorial da distância entre do ponto de aplicação e a referência e o vetor força. Como referência adotaremos o apoio fixo')
    for i in range(0, len(barra.forcas)): #soma dos momentos provocados pelas forças
        print('Momento da Força %d:' %(i+1))
        print('\t M = %dN.m' %((barra.forcas[i].posicaoX - barra.apoio[1].posicaoX)*barra.forcas[i].FY - (barra.forcas[i].posicaoY - barra.apoio[1].posicaoY)*barra.forcas[i].FX))
        M += (barra.forcas[i].posicaoX - barra.apoio[1].posicaoX)*barra.forcas[i].FY - (barra.forcas[i].posicaoY - barra.apoio[1].posicaoY)*barra.forcas[i].FX
    print()
    print('A soma é Mforças = %dN.m' %M)
    print()
    passar = input('Agora montaremos o sistema de equações! Digite qualquer coisa para continuar...')
    print()
    print('Nós temos o seguinte sistma:\nXfixo = -FX\nYsimples + Yfixo = -FY\nL^Ysimples = -(Mtotal + Mforças)\n\nSendo L o vetor distância do apoio simples ao apoio fixo')
    print()
    passar = input('Para ver a resposta digite qualquer coisa...')
    print()
    matriz = np.array([[0,1,0],[1,0,1],[(barra.apoio[0].posicaoX - barra.apoio[1].posicaoX),0,0]])
    resp = np.array([-sumFX, -sumFY, -(sumM + M)])
    x = np.linalg.solve(matriz,resp)
    barra.apoio[0].reacaoY = x[0]
    barra.apoio[1].reacaoX = x[1]
    barra.apoio[1].reacaoY = x[2]

    print('Reação Y do apoio simples: %dN' %barra.apoio[0].reacaoY)
    print('Reação X do apoio fixo: %dN' %barra.apoio[1].reacaoX)
    print('Reação Y do apoio fixo: %dN' %barra.apoio[1].reacaoY)

plt.close()



