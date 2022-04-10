from time import sleep


PAREDE = '#'
CAMINHO_LIVRE = ' '
CAMINHO_PERCORRIDO = "2"
ROBO = "4"
SAIDA = "S"

ESQUERDA = [0, -1]
DIREITA  = [0, 1]
CIMA     = [-1, 0]
BAIXO    = [1, 0]

LABIRINTO = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
    ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'], 
    ['#', '#', '#', '#', '#', '#', ' ', ' ', '4', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#'], 
    ['#', '#', '#', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'], 
    ['#', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', '#', ' ', '#'], 
    ['#', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#'], 
    ['#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', '#'], 
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'S', '#']
]


def print_labirinto():
    print("")
    for linha in LABIRINTO:
        print("".join(linha))
    print("")


def movimento(posicao: tuple, direcao: list):
    LABIRINTO[posicao[0]][posicao[1]] = CAMINHO_PERCORRIDO
    LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] = ROBO
    return [posicao[0] + direcao[0], posicao[1] + direcao[1]]
    

def verifica_movimento(posicao: tuple, direcao: list) -> bool:
    if LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] == SAIDA:
        raise print("SUCESSO")

    return (LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] == CAMINHO_LIVRE) 


def main():
    POSICAO_INICIAL = [3, 8]

    LABIRINTO[POSICAO_INICIAL[0]][POSICAO_INICIAL[1]] = ROBO

    print_labirinto()

    POSICAO_ATUAL = POSICAO_INICIAL

    if verifica_movimento(POSICAO_ATUAL, CIMA):
        POSICAO_ATUAL = movimento(POSICAO_ATUAL, CIMA)
        print_labirinto()
        sleep(1)

    if verifica_movimento(POSICAO_ATUAL, CIMA):
        POSICAO_ATUAL = movimento(POSICAO_ATUAL, CIMA)
        print_labirinto()
        sleep(1)

    if verifica_movimento(POSICAO_ATUAL, DIREITA):
        POSICAO_ATUAL = movimento(POSICAO_ATUAL, DIREITA)
        print_labirinto()
        sleep(1)   

    if verifica_movimento(POSICAO_ATUAL, DIREITA):
        POSICAO_ATUAL = movimento(POSICAO_ATUAL, DIREITA)
        print_labirinto()
        sleep(1)        

    if verifica_movimento(POSICAO_ATUAL, DIREITA):
        POSICAO_ATUAL = movimento(POSICAO_ATUAL, DIREITA)
        print_labirinto()
        sleep(1)        

    if verifica_movimento(POSICAO_ATUAL, DIREITA):
        POSICAO_ATUAL = movimento(POSICAO_ATUAL, DIREITA)
        print_labirinto()
        sleep(1)        

    if verifica_movimento(POSICAO_ATUAL, DIREITA):
        POSICAO_ATUAL = movimento(POSICAO_ATUAL, DIREITA)
        print_labirinto()
        sleep(1)        

    if verifica_movimento(POSICAO_ATUAL, DIREITA):
        POSICAO_ATUAL = movimento(POSICAO_ATUAL, DIREITA)
        print_labirinto()
        sleep(1)        

    if verifica_movimento(POSICAO_ATUAL, DIREITA):
        POSICAO_ATUAL = movimento(POSICAO_ATUAL, DIREITA)
        print_labirinto()
        sleep(1)        

    if verifica_movimento(POSICAO_ATUAL, DIREITA):
        POSICAO_ATUAL = movimento(POSICAO_ATUAL, DIREITA)
        print_labirinto()
        sleep(1)        

    if verifica_movimento(POSICAO_ATUAL, BAIXO):
        POSICAO_ATUAL = movimento(POSICAO_ATUAL, BAIXO)
        print_labirinto()
        sleep(1)   

    if verifica_movimento(POSICAO_ATUAL, BAIXO):
        POSICAO_ATUAL = movimento(POSICAO_ATUAL, BAIXO)
        print_labirinto()
        sleep(1)        

    if verifica_movimento(POSICAO_ATUAL, DIREITA):
        POSICAO_ATUAL = movimento(POSICAO_ATUAL, DIREITA)
        print_labirinto()
        sleep(1)        

    if verifica_movimento(POSICAO_ATUAL, DIREITA):
        POSICAO_ATUAL = movimento(POSICAO_ATUAL, DIREITA)
        print_labirinto()
        sleep(1)    

    if verifica_movimento(POSICAO_ATUAL, BAIXO):
        POSICAO_ATUAL = movimento(POSICAO_ATUAL, BAIXO)
        print_labirinto()
        sleep(1)   

    if verifica_movimento(POSICAO_ATUAL, BAIXO):
        POSICAO_ATUAL = movimento(POSICAO_ATUAL, BAIXO)
        print_labirinto()
        sleep(1)        

    if verifica_movimento(POSICAO_ATUAL, BAIXO):
        POSICAO_ATUAL = movimento(POSICAO_ATUAL, BAIXO)
        print_labirinto()
        sleep(1)   

    if verifica_movimento(POSICAO_ATUAL, BAIXO):
        POSICAO_ATUAL = movimento(POSICAO_ATUAL, BAIXO)
        print_labirinto()
        sleep(1)        

    if verifica_movimento(POSICAO_ATUAL, BAIXO):
        POSICAO_ATUAL = movimento(POSICAO_ATUAL, BAIXO)
        print_labirinto()
        sleep(1)   

    if verifica_movimento(POSICAO_ATUAL, BAIXO):
        POSICAO_ATUAL = movimento(POSICAO_ATUAL, BAIXO)
        print_labirinto()
        sleep(1)       
        

     
if __name__ == "__main__":
    main()

