def adicionar_aresta(gr, u, v, p):
    gr.append([u, v, p])

def encontrar_pai(pai, i):
    if pai[i] == i:
        return i
    return encontrar_pai(pai, pai[i])

def unir_conjuntos(pai, rank, x, y):
    raiz_x = encontrar_pai(pai, x)
    raiz_y = encontrar_pai(pai, y)
    if rank[raiz_x] < rank[raiz_y]:
        pai[raiz_x] = raiz_y
    elif rank[raiz_x] > rank[raiz_y]:
        pai[raiz_y] = raiz_x
    else:
        pai[raiz_y] = raiz_x
        rank[raiz_x] += 1

def algoritmo_kruskal(vertices, arestas):
    resultado = []
    arestas = sorted(arestas, key=lambda item: item[2])
    pai = list(range(vertices))
    rank = [0] * vertices
    e = 0
    for i in range(len(arestas)):
        u, v, p = arestas[i]
        x = encontrar_pai(pai, u)
        y = encontrar_pai(pai, v)
        if x != y:
            e += 1
            resultado.append([u, v, p])
            unir_conjuntos(pai, rank, x, y)
        if e == vertices - 1:
            break
    for u, v, peso in resultado:
        print("%d - %d: %d" % (u, v, peso))

grafo = []
adicionar_aresta(grafo, 0, 1, 4)
adicionar_aresta(grafo, 0, 2, 4)
adicionar_aresta(grafo, 1, 2, 2)
adicionar_aresta(grafo, 1, 0, 4)
adicionar_aresta(grafo, 2, 0, 4)
adicionar_aresta(grafo, 2, 1, 2)
adicionar_aresta(grafo, 2, 3, 3)
adicionar_aresta(grafo, 2, 5, 2)
adicionar_aresta(grafo, 2, 4, 4)
adicionar_aresta(grafo, 3, 2, 3)
adicionar_aresta(grafo, 3, 4, 3)
adicionar_aresta(grafo, 4, 2, 4)
adicionar_aresta(grafo, 4, 3, 3)
adicionar_aresta(grafo, 5, 2, 2)
adicionar_aresta(grafo, 5, 4, 3)

algoritmo_kruskal(6, grafo)
