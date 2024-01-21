import networkx as nx
import matplotlib.pyplot as plt

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        if isinstance(other, Ponto):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))
class Linha:
    def __init__(self, pontoA, pontoB, label):
        self.filhos = []
        self.pontoA = pontoA
        self.pontoB = pontoB
        self.label = label
    def addFilho(self, filho):
        self.filhos.append(filho)
    def __str__(self) -> str:
        return f'{self.label}'
    def __eq__(self, other):
        if isinstance(other, Linha):
            return self.pontoA == other.pontoA and self.pontoB == other.pontoB
        return False

class Grafo:
    def __init__(self):
        self.a = Linha(Ponto(1, 1), Ponto(1, 2), 'a')
        self.b = Linha(Ponto(1, 2), Ponto(2, 2), 'b')
        self.c = Linha(Ponto(2, 2), Ponto(2, 1), 'c')
        self.d = Linha(Ponto(2, 1), Ponto(1, 1), 'd')
        self.e = Linha(Ponto(1, 1), Ponto(2, 2), 'e')
        self.f = Linha(Ponto(2, 2), Ponto(1.5, 2.5), 'f')
        self.g = Linha(Ponto(1.5, 2.5), Ponto(1, 2), 'g')
        self.h = Linha(Ponto(1, 2), Ponto(2, 1), 'h')
        self.linhas = [self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h]
        for i in self.linhas:
            for y in self.linhas:
                if i != y:
                    if (i.pontoA == y.pontoA) or (i.pontoB == y.pontoB) or (i.pontoB == y.pontoA) or (i.pontoA == y.pontoB):
                        i.addFilho(y)
todosCaminhos = []
def completarGrafo(linhaIncial, caminhosVisitados, pontoAtual):
    caminhosVisitados.append(linhaIncial)
    if len(caminhosVisitados) == 8:
        todosCaminhos.append(caminhosVisitados.copy())
        caminhosVisitados.remove(linhaIncial)
        return 1
    total = 0
    for i in linhaIncial.filhos:
        if (i.pontoA == pontoAtual or i.pontoB == pontoAtual) and not any(i == linha for linha in caminhosVisitados):
            novoPonto = i.pontoB if i.pontoA == pontoAtual else i.pontoA
            total += completarGrafo(i, caminhosVisitados, novoPonto)
    caminhosVisitados.remove(linhaIncial)
    return total

grafo = Grafo()
caminhosVisitados = []

for i in grafo.linhas:
    completarGrafo(i, caminhosVisitados, i.pontoA)
    completarGrafo(i, caminhosVisitados, i.pontoB)


def plotarTodosCaminhos(todosCaminhos):
    for caminho in todosCaminhos:
        G = nx.Graph()
        pos = {}
        edge_labels = {}
        node_labels = {}
        ordem_linhas = ""
        for i, linha in enumerate(caminho):
            G.add_edge(linha.pontoA, linha.pontoB)
            pos[linha.pontoA] = (linha.pontoA.x, linha.pontoA.y)
            pos[linha.pontoB] = (linha.pontoB.x, linha.pontoB.y)
            edge_labels[(linha.pontoA, linha.pontoB)] = linha.label
            node_labels[linha.pontoA] = i+1
            node_labels[linha.pontoB] = i+2
            ordem_linhas += f"{i+1}. {linha.label}, "
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        nx.draw_networkx_labels(G, pos, labels=node_labels)
        plt.text(0.5, -0.1, ordem_linhas[:-2], horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
        plt.show()


plotarTodosCaminhos(todosCaminhos)



                    
                    