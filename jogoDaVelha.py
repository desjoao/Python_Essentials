from random import randrange


def imprimirTabuleiro(tabuleiro):
	print("+-------" * 3,"+", sep="") 
	for linha in range(3):
		print("|       " * 3,"|", sep="")
		for coluna in range(3):
			print("|   " + str(tabuleiro[linha][coluna]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")


def movimento(tabuleiro):
	ok = False	# suposição falsa - precisamos dela para entrar no loop
	while not ok:
		move = input("Digite seu movimento: ") 
		ok = len(move) == 1 and move >= '1' and move <= '9' # a entrada do usuário é válida?
		if not ok:
			print("Má jogada – repita sua entrada!") # não, não é - faça a entrada novamente
			continue
		move = int(move) - 1 	# número de célula de 0 a 8
		linha = move // 3 	# linha da célula
		coluna = move % 3		# coluna da célula
		valor = tabuleiro[linha][coluna]	# verifica o quadrado selecionado
		ok = valor not in ['O','X'] 
		if not ok:	#está ocupado - para a entrada novamente
			print("Campo já ocupado – repita sua entrada!")
			continue
    tabuleiro[linha][coluna] = 'O' 	# define '0' no quadrado selecionado


def camposLivres(tabuleiro):
	livres = []	
	for linha in range(3): # iterar pelas linhas
		for coluna in range(3): # iterar pelas colunas
			if tabuleiro[linha][coluna] not in ['O','X']: # o celular está livre?
				livres.append((linha,coluna)) # sim, é - anexe uma nova tupla à lista
	return livres


def defineVencedor(tabuleiro, valor):
	if valor == "X":	# estamos procurando por X?
		quem = 'eu'	# sim - é do lado do computador
	elif valor == "O": # ... ou para O?
		quem = 'voce'	# sim - é o nosso lado
	else:
		quem = None	# não devemos cair aqui!
	diagonal1 = diagonal2 = True  # para diagonais
	for lincol in range(3):
		if tabuleiro[lincol][0] == valor and tabuleiro[lincol][1] == valor and tabuleiro[lincol][2] == valor:	# verifica a linha lincol
			return quem
		if board[0][lincol] == valor and tabuleiro[1][lincol] == valor and tabuleiro[2][lincol] == valor: # verifica a coluna lincol
			return quem
		if tabuleiro[lincol][lincol] != valor: # verifica a 1ª diagonal
			diagonal1 = False
		if tabuleiro[2 - lincol][2 - lincol] != valor: # verifica a segunda diagonal
			digonal2 = False
	if diagonal or diagonal:
		return quem
	return None


def movimenta(tabuleiro):
	livres = camposLivres(tabuleiro) #faça uma lista de campos livres
	cnt = len(free)
	if cnt > 0:	
		this = randrange(cnt)
		linha, coluna = livres[this]
		tabuleiro[linha][coluna] = 'X'

tabuleiro = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] 
tabuleiro[1][1] = 'X' # coloca primeiro 'X' no meio
livres = camposLivres(tabuleiro)
turno = True # que turno é agora?
while len(livres):
	imprimirTabuleiro(tabuleiro)
	if turno:
		movimento(board)
		vencedor = defineVencedor(tabuleiro,'O')
	else:	
		movimenta(tabuleiro)
		vencedor = defineVencedor(tabuleiro,'X')
	if vencedor != None:
		break
	turno = not turno
	livres = camposLivres(tabuleiro)

imprimirTabuleiro(tabuleiro)
if vencedor == 'voce':
	print("Você venceu!")
elif vencedor == 'eu':
	print("Eu venci")
else:
	print("Empate!")
