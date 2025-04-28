class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserir(self, valor, pos):
        novo = No(valor)
        if pos <= 0 or not self.head:
            novo.prox = self.head
            self.head = novo
            return
        atual = self.head
        indice = 0
        while atual.prox and indice < pos - 1:
            atual = atual.prox
            indice += 1
        novo.prox = atual.prox
        atual.prox = novo

    def remover(self, valor):
        atual = self.head
        anterior = None
        while atual:
            if atual.valor == valor:
                if anterior:
                    anterior.prox = atual.prox
                else:
                    self.head = atual.prox
                return
            anterior = atual
            atual = atual.prox

    def imprimir(self):
        atual = self.head
        valores = []
        while atual:
            valores.append(str(atual.valor))
            atual = atual.prox
        print(' '.join(valores))


## LEITURA DO ARQUIVO txt

with open('arq.txt', 'r', encoding='utf-8-sig') as f:
    linhas = f.readlines()

valores_iniciais = list(map(int, linhas[0].split()))
qtd = int(linhas[1])
comandos = [linha.strip() for linha in linhas[2:]]

lista = ListaEncadeada()
for v in reversed(valores_iniciais):
    lista.inserir(v, 0)

for comando in comandos:
    if not comando:
        continue
    partes = comando.split()
    if partes[0] == 'A':
        valor = int(partes[1])
        pos = int(partes[2])
        lista.inserir(valor, pos)
    elif partes[0] == 'R':
        valor = int(partes[1])
        lista.remover(valor)
    elif partes[0] == 'P':
        lista.imprimir()
