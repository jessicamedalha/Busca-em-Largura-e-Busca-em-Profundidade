import random
import numpy as np
import math
from numpy import loadtxt
from random import sample

class filas_de_busca(object):

	def __init__(self):
		self.fila_pai = []
		self.fila_filhos = []
		self.ptr_pai = []
		self.ptr_filho = []


	def add_pai(self,elemento, posicao_i, posicao_j):
		if(elemento == 1):
			self.fila_pai.append(posicao_i + 1)
			self.fila_pai.append(posicao_j)
		if(elemento == 2):	
			self.fila_pai.append(posicao_i - 1)
			self.fila_pai.append(posicao_j)
		if(elemento == 3):
			self.fila_pai.append(posicao_i)
			self.fila_pai.append(posicao_j + 1)	
		if(elemento == 4):
			self.fila_pai.append(posicao_i)
			self.fila_pai.append(posicao_j - 1)

	def add_filho(self,elemento, posicao_i, posicao_j):
		print("aqui")
		if(elemento == 1):
			self.fila_filhos.append(posicao_i + 1)
			self.fila_filhos.append(posicao_j)
		if(elemento == 2):	
			self.fila_filhos.append(posicao_i - 1)
			self.fila_filhos.append(posicao_j)
		if(elemento == 3):
			self.fila_filhos.append(posicao_i)
			self.fila_filhos.append(posicao_j + 1)	
		if(elemento == 4):
			self.fila_filhos.append(posicao_i)
			self.fila_filhos.append(posicao_j - 1)

	def remove_pai(self):
		self.fila_pai.pop(0)
		self.fila_pai.pop(0)
	def remove_filho(self):
		self.fila_filhos.pop(0)
		self.fila_filhos.pop(0)


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

		self.filas = filas_de_busca()

		self.labirinto = np.loadtxt('labirinto.dat', dtype='int', delimiter='	')
		self.ponto_de_partida()


	def ponto_de_partida(self):
		for i in range(len(self.labirinto)):
			for j in range(len(self.labirinto)):
				if(self.labirinto[i][j] == self.entrada):
					self.posicao_i = i
					self.posicao_j = j 

		self.percorre_labirinto()

					

	def percorre_labirinto(self): #acaminha pelo labirinto
		while(1):
			num_direcoes = self.tem_direcoes(self.posicao_i, self.posicao_j ) 
			##print("numero de direcoes",num_direcoes)
			if( num_direcoes != 0 ): #tem direções disponiveis para andar
				self.direcoes = sample(range(1, 5), 4) #vetor com indices aleatorios de direções
				#print(self.direcoes)
				for i in range(len(self.direcoes)): 
					netos = self.verifica_direcao(self.direcoes[i], num_direcoes) #verifica se a direção ta disponivel para andar
					print("netos", netos)
					if( netos >= 0):#se ta disponivel para andar
						posicao_i = self.posicao_i
						posicao_j = self.posicao_j

						self.filas.add_filho(self.direcoes[i], self.posicao_i, self.posicao_j)
						if(netos == 0):# se a direção é caminha sem saida
							self.filas.remove_filho()
						elif(netos > 0):# se a direção possui outros caminhos abertos
							self.filas.add_pai(self.direcoes[i], self.posicao_i, self.posicao_j)
							self.filas.remove_filho()
							print("pai",self.filas.fila_pai)
							print("filhos2",self.filas.fila_filhos)

				self.labirino [self.posicao_i][self.posicao_j] = self.pegada
				self.proximo_pai_fila()

			'''else: #naõ tem direções disponiveis para andar
				self.volta_direcao_anterior()'''
			break


	def tem_direcoes(self, posicao_i, posicao_j):# verifica se há direções disponivel e retonar as direções disponiveis
		contador = 0
		#baixo
		if((self.labirinto[posicao_i + 1][posicao_j] == self.caminho) or (self.labirinto[posicao_i + 1][posicao_j] == self.saida)):
			contador+=1

		#cima
		elif((self.labirinto[posicao_i - 1][posicao_j] == self.caminho) or (self.labirinto[posicao_i - 1][posicao_j] == self.saida)):
			contador+= 10

		#direita
		elif((self.labirinto[posicao_i][posicao_j + 1] == self.caminho) or (self.labirinto[posicao_i ][posicao_j + 1] == self.saida)):
			contador += 100


		#esquerda
		elif((self.labirinto[posicao_i][posicao_j - 1] == self.caminho) or (self.labirinto[posicao_i ][posicao_j - 1] == self.saida)):
			contador += 1000

		return contador 

	def verifica_direcao(self,i, num_direcoes): # verifica se na direções é possivel caminhar e se elas são ou não caminho sem saida
		j = 1000
		retorno = 0
		print(i, num_direcoes)
		for k in range (4,0, -1):
			'''print("k",k)
			print("num_direcoes",num_direcoes)
			print("j",j)
			print("div",int(num_direcoes/j))'''
			if((int(num_direcoes/j)) == 1):
				num_direcoes = num_direcoes - j
				#print("num_direcoes", num_direcoes)

				if((k) == i):
					if(i == 1):
						retorno = self.tem_direcoes((self.posicao_i + 1), self.posicao_j)
						print("retorno:", retorno)
						return retorno
						#break
					elif(i == 2):
						retorno = self.tem_direcoes((self.posicao_i - 1), self.posicao_j)
						print("retorno:", retorno)
						return retorno
						#break
					elif(i == 3):
						retorno = self.tem_direcoes((self.posicao_i ), (self.posicao_j + 1))
						print("retorno:", retorno)
						return retorno
						#break
					elif(i == 4):
						retorno = self.tem_direcoes((self.posicao_i), (self.posicao_j - 1))
						print("retorno:", retorno)
						return retorno
						#break
	
			j = 10**((math.log10(j))-1)
			#print("retorno:", retorno)
		return retorno



		

	'''def proximo_pai_fila():##ponteiro para fila pai, arrumar
		self.posicao_i = fila_pai[self.ptr_pai + 1]
		self.posicao_j= fila_pai[self.ptr_pai + 2]
		'''




