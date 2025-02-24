from tkinter import *
import sys, threading
from os import system
from time import sleep


def inicio_jogo():
    global matriz, contagem_estagio

    def verificar_volta(xp, yp, valor):
        vizinhas = 0

        for x in range(xp-1, xp+2):
            for y in range(yp-1, yp+2):
                if (x, y) == (xp, yp):
                    continue
                try:
                    if x >= 0 and y >= 0:
                        if matriz[x][y] == '1':
                            vizinhas += 1
                except:
                    continue
        if valor == '1':
            if vizinhas in [2, 3]:
                return '1'
            else:
                return '0'
        else:
            if vizinhas == 3:
                return '1'
            else:
                return '0'

    infinito = False
    cont = 1
    temp_matriz = []
    while True:
        matriz_nova = []
        if not infinito:
            contagem_estagio += 1
            estagio['text'] = f'{contagem_estagio:03.0f}'
        for ix, x in enumerate(matriz):
            linha = ''
            for iy, y in enumerate(x):
                valor = verificar_volta(ix, iy, y)
                linha += valor
                tabuleiro[ix][iy]['bg'] = 'black' if valor == '1' else 'gray90'
            matriz_nova.append(linha)
        if matriz_nova == matriz:
            estagio.configure(text='INFINITO', fg='red', bg='gray60', font='Impact')
            estagio.place(x=dimensao*tamanho_botao+tamanho_botao-30)
            infinito = True
        elif cont == 1:
            temp_matriz = list(matriz_nova)
        elif cont == 3:
            if matriz_nova == temp_matriz:
                estagio.configure(text='INFINITO', fg='red', bg='gray60', font='Impact')
                estagio.place(x=dimensao*tamanho_botao+tamanho_botao-30)
                infinito = True
            else:
                cont = 1
                temp_matriz = list(matriz_nova)

        matriz = list(matriz_nova)
        cont += 1
        sleep(0.5)

def clicar(botao):
    botao['bg'] = 'black' if botao['bg'] == 'gray90' else 'gray90'
    botao['activebackground'] = 'gray15' if botao['activebackground'] == 'gray75' else 'gray75'

def comecar(botao):
    global matriz

    botao['state'] = DISABLED
    matriz = []
    for x in range(dimensao):
        linha = ''
        for y in range(dimensao):
            linha += '1' if tabuleiro[x][y]['bg'] == 'black' else '0'
            tabuleiro[x][y]['state'] = DISABLED
        matriz.append(linha)
    
    
    thread = threading.Thread(target=inicio_jogo)
    thread.daemon = True
    thread.start()

while True:
    try:
        print('Digite a dimensão do tabuleiro:')
        dimensao = int(sys.stdin.readline())
        if dimensao < 4:
            print('Digite no mínimo 4')
            continue
        break
    except:
        print('Digite um número inteiro')

try: system('cls')
except: system('clear')

tabuleiro = []
for x in range(dimensao):
    tabuleiro.append([])

window = Tk()
window.title('Jogo da Vida de Conway')
window.resizable(False, False)
tamanho_botao = 30
window.geometry(f'{dimensao*tamanho_botao+tamanho_botao*2+5}x{dimensao*tamanho_botao}')
b = Button(window, text='COMEÇAR', fg='black', bg='green3', font='Impact', activebackground='green')
b.place(x=dimensao*tamanho_botao, y=0, height=30, width=tamanho_botao*2+5)
b['command'] = lambda botao = b: comecar(botao)
Label(window, bg='gray60').place(x=dimensao*tamanho_botao, y=tamanho_botao, height=dimensao*tamanho_botao, width=tamanho_botao*2+5)
Label(window, text='ESTAGIO:', fg='black', bg='gray60', font='Impact').place(x=dimensao*tamanho_botao, y=tamanho_botao* int(dimensao/2))
contagem_estagio = 0
estagio = Label(window, text='000', fg='blue2', bg='gray60', font='Impact')
estagio.place(x=dimensao*tamanho_botao+tamanho_botao-15, y=tamanho_botao* (int(dimensao/2)+1))

for l in range(dimensao):
    for c in range(dimensao):
        posX = c * tamanho_botao
        posY = l * tamanho_botao
        b = Button(window, activebackground='gray75', bg='gray90')
        b['command'] = lambda botao = b: clicar(botao)
        b.place(x=posX, y=posY, height=tamanho_botao, width=tamanho_botao)
        tabuleiro[l].append(b)

window.mainloop()
