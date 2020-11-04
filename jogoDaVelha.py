board = [' ' for x in range(10)]

#Inserir uma letra em uma dada posicao
def insertLetter(letter, pos):
    board[pos] = letter

#Verificar se o espaco escolhido esta vazio
def spaceIsFree(pos):
    return board[pos] == " "

#Printar o tabuleiro na tela
def printBoard(board):
    print(" " + board[1] + "/ " + board[2] + "/ " + board[3])
    print("---------")
    print(" " + board[4] + "/ " + board[5] + "/ " + board[6])
    print("---------")
    print(" " + board[7] + "/ " + board[8] + "/ " + board[9])

#Verifica se ha um vencedor
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or
            (bo[3] == le and bo[5] == le and bo[7] == le))

#Pede uma posicao de jogada ao usuario, verifica se ela possivel e a posiciona
def playMove():
    run = True
    while run:
        move = input("Selecione uma posicao para X (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10 :
                if spaceIsFree(move):
                    run = False
                    insertLetter("x", move)
                else:
                    print("Esse espaco esta oculpado")
            else:
                print("Selecione um numero entre 1 e 9")
        except:
            print("Selecione um numero. ")

#Funcao de jogada do computador
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    if 5 in possibleMoves:
        move = 5
        return move
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    return move

#Funcao para gerar um aleatorio e seleciona-lo
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

#Verifica se o tabuleiro esta cheio
def isBoardFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True

def main():
    print("JOGO DA VELHA")
    printBoard(board)
    while not(isBoardFull(board)):
        if not(isWinner(board, "O")):
            playMove()
            printBoard(board)
        else:
            print("O PC ganhou dessa vez! ")
            break
        if not(isWinner(board, "X")):
            move  = compMove()
            if move == 0:
                print("Empate!")
            else:
                insertLetter("o", move)
                print("Computador marcou na posicao", move, ":")
                printBoard(board)
        else:
            print("Voce ganhou, parabens!")
            break
    if isBoardFull(board):
        print("Empate")

main()