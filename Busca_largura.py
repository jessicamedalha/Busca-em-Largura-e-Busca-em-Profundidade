import random
import numpy as np
import math
from numpy import loadtxt

class filas_de_busca():

	def __init__(self):
		self.fila_pai = []
		self.fila_filhos = []
		self.ptr_pai
		self.ptr_filho


	def add_pai(elemento):
		if(elemento == 1):
			fila_pai.append(self.posicao_i + 1)
			fila_pai.append(posicao_j)
		if(elemento == 2):	
			fila_pai.append(self.posicao_i - 1)
			fila_pai.append(posicao_j)
		if(elemento == 3):
			fila_pai.append(self.posicao_i)
			fila_pai.append(posicao_j + 1)	
		if(elemento == 4):
			fila_pai.append(self.posicao_i)
			fila_pai.append(posicao_j - 1)

	def add_fiho(elemento):
		if(elemento == 1):
			fila_filhos.append(self.posicao_i + 1)
			fila_filhos.append(posicao_j)
		if(elemento == 2):	
			fila_filhos.append(self.posicao_i - 1)
			fila_filhos.append(posicao_j)
		if(elemento == 3):
			fila_filhos.append(self.posicao_i)
			fila_filhos.append(posicao_j + 1)	
		if(elemento == 4):
			fila_filhos.append(self.posicao_i)
			fila_filhos.append(posicao_j - 1)

	def remove_pai():
		fila_pai.pop(0)
		fila_pai.pop(0)
	def remove_filho():
		fila_filhos.pop(0)
		fila_filhos.pop(0)


class busca_largura():
	def __init__(self):
		self.entrada = 2
		self.saida = 3
		self.parede = 0
		self.caminho = 1
		self.direcoes = []
		self.pegada = 5

		self.posicao_i = 0
		self.posicao_j = 0

		#print("aqui")
		#arq = open("labirinto.dat", "r+")
		self.labirinto = np.loadtxt('labirinto.dat', dtype='int', delimiter='	')
		self.ponto_de_partida()


	def ponto_de_partida(self):
		for i in range(len(self.labirinto)):
			for j in range(len(self.labirinto)):
				if(self.labirinto[i][j] == self.entrada):
					self.posicao_i = i
					self.posicao_j = j 
					print (self.posicao_i)
					print (self.posicao_j)
					

	'''def percorre_labirinto(self): #acaminha pelo labirinto
		while(True):

			num_direcoes = self.tem_direcoes(self.posicao_i, self.posicao_j ) 
			if( num_direcoes != 0 ): #tem direções disponiveis para andar
				self.direcoes = sample(range(0, 5), 4) #vetor com indices aleatorios de direções
				for i in range(len(self.direcoes)): 
					netos = self.verifica_direcao(direcoes[i], num_direcoes) #verifica se a direção ta disponivel para andar
					if( netos >= 0):#se ta disponivel para andar
						self.add_filho(i)
						if(netos == 0):# se a direção é caminha sem saida
							self.remove_filho()
						elif(netos > 0):# se a direção possui outros caminhos abertos
							self.add_pai(i)
							self.remove_filho()

				self.labirino [self.posicao_i][self.posicao_j] = self.pegada
				self.proximo_pai_fila()

			else: #naõ tem direções disponiveis para andar
				self.volta_direcao_anterior()


	def tem_direcoes(posicao_i, posicao_j):# verifica se há direções disponivel e retonar as direções disponiveis
		contador = 0
		#direita
		if((self.labirinto[posicao_i + 1][posicao_j] == self.caminho) or (self.labirinto[posicao_i + 1][posicao_j] == self.saida)):
			contador+=1

		#esquerda
		elif((self.labirinto[posicao_i - 1][posicao_j] == self.caminho) or (self.labirinto[posicao_i - 1][posicao_j] == self.saida)):
			contador+= 10

		#cima
		elif((self.labirinto[posicao_i][posicao_j + 1] == self.caminho) or (self.labirinto[posicao_i ][posicao_j + 1] == self.saida)):
			contador += 100


		#baixo
		elif((self.labirinto[posicao_i][posicao_j - 1] == self.caminho) or (self.labirinto[posicao_i ][posicao_j - 1] == self.saida)):
			contador += 1000

		return contador 

	def verifica_direcao(i, num_direcoes): # verifica se na direções é possivel caminhar e se elas são ou não caminho sem saida
		j = 1000
		for k in range 4:
			if((int(num_direcoes/j)) == 1):
				num_direcoes = num_direcoes - j

				if((k+1) == i):

					if(i == 1):
						retorno = tem_direcoes((self.posicao_i + 1), self.posicao_j)
					elif(i == 2):
						retorno = tem_direcoes((self.posicao_i - 1), self.posicao_j)
					elif(i == 3):
						retorno = tem_direcoes((self.posicao_i ), (self.posicao_j + 1))
					elif(i == 4):
						retorno = tem_direcoes((self.posicao_i), (self.posicao_j - 1))
	
			j = 10**(math.log(j)-1) 

		return retorno

	def proximo_pai_fila():##ponteiro para fila pai, arrumar
		self.posicao_i = fila_pai[self.ptr_pai + 1]
		self.posicao_j= fila_pai[self.ptr_pai + 2]
		'''




