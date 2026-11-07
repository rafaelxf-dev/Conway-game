# 🧬 Jogo da Vida de Conway (Conway's Game of Life - Python GUI)

Implementação interativa do famoso autômato celular criado pelo matemático John Conway, desenvolvida em Python utilizando a biblioteca gráfica **Tkinter**, matrizes dinâmicas e gerenciamento de execução em segundo plano com **Threads**.

---

## 📌 Funcionalidades e Mecânicas

- **Configuração Inicial Customizável via Terminal:** O usuário define a dimensão do tabuleiro dinamicamente antes de abrir a interface gráfica (com validação para tamanhos mínimos).
- **Tabuleiros Interativos:** Células vivas e mortas configuráveis por cliques diretos na grade visual antes de iniciar a simulação.
- **Motor de Regras do Jogo da Vida:**
  - *Sobrevivência:* Células vivas com 2 ou 3 vizinhos continuam vivas.
  - *Nascimento:* Células mortas com exatamente 3 vizinhos tornam-se vivas.
  - *Morte:* Demais células morrem por solidão ou superpopulação.
- **Detecção Automática de Padrões Infinitos/Estáveis:** O sistema monitora ciclos e estados da matriz em tempo real para identificar padrões estacionários ou osciladores, sinalizando visualmente com o status **"INFINITO"**.
- **Contador de Estágios:** Acompanhamento contínuo das gerações/evoluções do autômato na barra lateral.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Interface Gráfica (GUI):** Tkinter
- **Concorrência:** `threading` para rodar o loop de evolução celular sem travar a interface da janela principal.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o Python 3 instalado no seu computador. Como o projeto utiliza exclusivamente bibliotecas nativas, nenhuma instalação de pacotes externos via pip é necessária.

### 1. Clonar o repositório
```
git clone https://github.com/rafaelxf-dev/Conway-game.git
cd Conway-game
```

### 2. Executar a aplicação
Inicie o script pelo terminal (ele solicitará a dimensão do tabuleiro no prompt de comando):
```
python conway.py
```
