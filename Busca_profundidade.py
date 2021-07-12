import numpy as np
import random
from numpy import loadtxt

class busca_profundidade():
	def __init__(self):

		self.entrada = 2
		self.saida = 3
		self.parede = 0
		self.pegada = 5
		self.posicaoAtualI = -1
		self.posicaoAtualJ = -1
		self.custoCaminho = [0]
		self.caminhoPercorrido = []
		self.passoAnterior = [-1, -1]
		self.posicaoInicialI = -1
		self.posicaoInicialJ = -1

		self.lab = self.seleciona_labirinto()

		self.labirinto = np.loadtxt(self.lab, dtype='int', delimiter='	')
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
			for j in range(len(self.labirinto[0])):
				if (self.labirinto[i][j] == self.entrada):

					self.posicaoAtualI = i
					self.posicaoAtualJ = j
					self.posicaoInicialI = i
					self.posicaoInicialJ = j
					i = len(self.labirinto)-1
					j = len(self.labirinto[0])-1

					self.percorre_labirinto()

	def percorre_labirinto(self):
		if self.posicaoAtualI == -1 and self.posicaoAtualJ == -1:
			print('Não existe posição inicial dentro do labirinto!')
		else:
			while self.verificaFinal() == False:
				caminhos = self.verifica_CaminhoPossivel()
				passo = self.proximoPasso(caminhos)
				self.passoAnterior = [self.posicaoAtualI, self.posicaoAtualJ]
				self.posicaoAtualI, self.posicaoAtualJ = self.anda(passo[0], passo[1])

		print('Busca por Profundidade:')
		print(f'Estado inicial: {self.posicaoInicialI} linha {self.posicaoInicialJ} coluna')
		print(f'Custo de caminho: {self.custoCaminho[0]}')
		print(f'Custo de passo: {self.custoCaminho[0]}')
		print(f'Caminho percorridos: {self.caminhoPercorrido}')
		print('Labirinto:')
		print(self.labirinto)

	def verificaFinal(self):
		return self.labirinto[self.posicaoAtualI][self.posicaoAtualJ] == self.saida

	def verifica_CaminhoPossivel(self): 
		caminhosPossiveis = []

		if (self.posicaoAtualI) < len(self.labirinto)-1:
			if self.labirinto[(self.posicaoAtualI)+1][self.posicaoAtualJ] != 0:
				caminhosPossiveis.append([self.posicaoAtualI+1, self.posicaoAtualJ])
		if self.posicaoAtualJ < len(self.labirinto[0])-1:
			if self.labirinto[self.posicaoAtualI][self.posicaoAtualJ+1] != 0:
				caminhosPossiveis.append([self.posicaoAtualI, self.posicaoAtualJ+1])
		if self.posicaoAtualI > 0:
			if self.labirinto[self.posicaoAtualI-1][self.posicaoAtualJ] != 0:
				caminhosPossiveis.append([self.posicaoAtualI-1, self.posicaoAtualJ])
		if self.posicaoAtualJ > 0:
			if self.labirinto[self.posicaoAtualI][self.posicaoAtualJ-1] != 0:
				caminhosPossiveis.append([self.posicaoAtualI, self.posicaoAtualJ-1])

		return caminhosPossiveis

	def proximoPasso(self,caminhos):
		aux = 0
		if len(caminhos) > 1:
			while aux < len(caminhos):
				if caminhos[aux] == self.passoAnterior:
					caminhos.pop(aux)
				aux += 1
		return caminhos[random.randint(0, len(caminhos)-1)]

	def anda(self,posicaoAvancoI, posicaoAvancoJ): 

		self.caminhoPercorrido.append([self.posicaoAtualI, self.posicaoAtualJ])
		self.labirinto[self.posicaoAtualI][self.posicaoAtualJ] = self.saida
		self.custoCaminho[0] += 1

		return posicaoAvancoI, posicaoAvancoJ

