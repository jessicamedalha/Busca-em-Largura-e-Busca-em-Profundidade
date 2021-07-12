import random
import numpy as np
import math
from numpy import loadtxt
from random import sample

class filas_de_busca(object): #filas que guardam a localização do nós e seus filhos

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
		if(elemento == 1):
			self.fila_filhos.append(posicao_i + 1)
			self.fila_filhos.append(posicao_j)
			return posicao_i + 1, posicao_j
			
		if(elemento == 2):	
			self.fila_filhos.append(posicao_i - 1)
			self.fila_filhos.append(posicao_j)
			return posicao_i - 1, posicao_j
			
		if(elemento == 3):
			self.fila_filhos.append(posicao_i)
			self.fila_filhos.append(posicao_j + 1)	
			return posicao_i, posicao_j +1
			
		if(elemento == 4):
			self.fila_filhos.append(posicao_i)
			self.fila_filhos.append(posicao_j - 1)
			return posicao_i, posicao_j - 1
			

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
		self.custoCaminho = [0]
		self.caminhoPercorrido = []

		self.posicao_i = 0
		self.posicao_j = 0
		self.posicaoInicialI = 0
		self.posicaoInicialJ = 0

		self.filas = filas_de_busca()

		self.lab = self.seleciona_labirinto()

		self.labirinto = np.loadtxt( self.lab, dtype='int', delimiter='	')
		self.ponto_de_partida()

	def seleciona_labirinto(self):
		while(1):
			a = input("Digite o número do labirinto que você deseja percorrer (1,2,3 ou 4): ")
			if(a == '1'):
				return 'Labirintos/labirinto_1.dat'
			elif(a == '2'):
				return 'Labirintos/labirinto_2.dat'
			elif(a == '3'):
				return 'Labirintos/labirinto_3.dat'
			elif(a == '4'):
				return 'Labirintos/labirinto_4.dat'

	def ponto_de_partida(self):
		for i in range(len(self.labirinto)):
			for j in range(len(self.labirinto)):
				if(self.labirinto[i][j] == self.entrada):
					self.posicao_i = i
					self.posicaoInicialI = i
					self.posicao_j= j 
					self.posicaoInicialJ = j

		self.percorre_labirinto()

	def percorre_labirinto(self): #acaminha pelo labirinto
		while(1):

			num_direcoes = self.tem_direcoes(self.posicao_i, self.posicao_j ) 
			#print("numero de direcoes",num_direcoes, self.posicao_i, self.posicao_j )
			if( num_direcoes != 0 and num_direcoes != 3): #tem direções disponiveis para andar

				self.direcoes = sample(range(1, 5), 4) #vetor com indices aleatorios de direções
				self.custoCaminho[0] += 1
				self.caminhoPercorrido.append([self.posicao_i, self.posicao_j])
				for i in range(len(self.direcoes)): 

					netos = self.verifica_direcao(self.direcoes[i], num_direcoes) #verifica se a direção ta disponivel para andar
					if( netos >= 0):#se ta disponivel para andar
						posicao_i = self.posicao_i
						posicao_j = self.posicao_j

						self.filas.add_filho(self.direcoes[i], self.posicao_i, self.posicao_j)
						if(netos == 0):# se a direção é caminha sem saida
							self.filas.remove_filho()

						elif(netos > 0):# se a direção possui outros caminhos abertos
							self.filas.add_pai(self.direcoes[i], self.posicao_i, self.posicao_j)
							self.filas.remove_filho()

				self.labirinto [self.posicao_i][self.posicao_j] = self.pegada
				self.proximo_pai_fila()
				#print(self.labirinto)
				#print("\n")
				#print("pai",self.filas.fila_pai)
				#print("filhos2",self.filas.fila_filhos)

			elif(num_direcoes == 3):
				self.labirinto [self.posicao_i][self.posicao_j] = self.pegada
				print('Busca por Largura:')
				print(f'Estado inicial: {self.posicaoInicialI} linha {self.posicaoInicialJ} coluna')
				print(f'Custo de caminho: {self.custoCaminho}')
				print(f'Custo de passo: {self.custoCaminho}')
				print(f'Caminho percorridos: {self.caminhoPercorrido}')
				print('Labirinto:')
				print(self.labirinto)
				break

			else: #naõ tem direções disponiveis para andar
				#print("pai",self.filas.fila_pai)
				#print("filhos2",self.filas.fila_filhos)
				self.labirinto [self.posicao_i][self.posicao_j] = self.pegada
				self.proximo_pai_fila()
				#break
				#self.filas.remove_pai()
				#self.posicao_i = self.filas.fila_pai[0]
				#self.posicao_j= self.filas.fila_pai[1]

	def tem_direcoes(self, posicao_i, posicao_j):# verifica se há direções disponivel e retonar as direções disponiveis
		contador = 0
		#baixo
		if((posicao_i+1 <= len(self.labirinto)-1 and self.labirinto[posicao_i + 1][posicao_j] == self.caminho) or (posicao_i+1 <= len(self.labirinto)-1 and self.labirinto[posicao_i + 1][posicao_j] == self.saida)):
			contador+=1
			if((self.labirinto[posicao_i + 1][posicao_j] == self.saida)):
				contador = 3
				return contador

		#cima
		if((posicao_i-1 >= 0 and self.labirinto[posicao_i - 1][posicao_j] == self.caminho) or (posicao_i-1 >= 0 and self.labirinto[posicao_i - 1][posicao_j] == self.saida)):
			contador+= 10
			if(self.labirinto[posicao_i - 1][posicao_j] == self.saida):
				contador = 3
				return contador

		#direita
		if((posicao_j+1 <= len(self.labirinto)-1 and self.labirinto[posicao_i][posicao_j + 1] == self.caminho) or (posicao_j+1 <= len(self.labirinto)-1 and self.labirinto[posicao_i ][posicao_j + 1] == self.saida)):
			contador += 100
			if(self.labirinto[posicao_i ][posicao_j + 1] == self.saida):
				contador = 3
				return contador 


		#esquerda
		if((posicao_j-1 >= 0 and self.labirinto[posicao_i][posicao_j - 1] == self.caminho) or (posicao_j-1 >= 0 and self.labirinto[posicao_i ][posicao_j - 1] == self.saida)):
			contador += 1000
			if(self.labirinto[posicao_i ][posicao_j - 1] == self.saida):
				contador = 3
				return contador 

		return contador 

	def verifica_direcao(self,i, num_direcoes): # verifica se na direções é possivel caminhar e se elas são ou não caminho sem saida
		j = 1000
		retorno = 0

		for k in range (4,0, -1):
			if((int(num_direcoes/j)) == 1):
				num_direcoes = num_direcoes - j

				if((k) == i):
					if(i == 1):
						retorno = self.tem_direcoes((self.posicao_i + 1), self.posicao_j)
						return retorno
					
					elif(i == 2):
						retorno = self.tem_direcoes((self.posicao_i - 1), self.posicao_j)
						return retorno
						
					elif(i == 3):
						retorno = self.tem_direcoes((self.posicao_i ), (self.posicao_j + 1))
						return retorno
						
					elif(i == 4):
						retorno = self.tem_direcoes((self.posicao_i), (self.posicao_j - 1))
						return retorno
						
	
			j = 10**((math.log10(j))-1)
		return retorno	

	def proximo_pai_fila(self):##ponteiro para fila pai
		self.posicao_i = self.filas.fila_pai[0]
		self.posicao_j= self.filas.fila_pai[1]
		self.filas.remove_pai()


		




