INFINITO = 9999999

num_vertices = 5

grafo = [[1, 2, 87, 4, 7],
         [54, 87, 45, 22, 33],
         [34, 92, 5, 55, 23],
         [13, 15, 99, 24, 25],
         [18, 19, 76, 87, 0]]

selecionado = [False] * num_vertices

num_arestas = 0

selecionado[0] = True

print("Aresta : Peso\n")

while num_arestas < num_vertices - 1:
    minimo = INFINITO
    x = 0
    y = 0
    for i in range(num_vertices):
        if selecionado[i]:
            for j in range(num_vertices):
                if not selecionado[j] and grafo[i][j]:
                    if minimo > grafo[i][j]:
                        minimo = grafo[i][j]
                        x = i
                        y = j
    print(f"{x}-{y}:{grafo[x][y]}")
    selecionado[y] = True
    num_arestas += 1
