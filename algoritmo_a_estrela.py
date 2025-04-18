import heapq

ROWS, COLS = 10, 10

# Mapa fixo com obstáculos
mapa_base = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '.', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '.', '#', '#', '#', '.', '#', '.'],
    ['.', '.', '#', '.', '.', '.', '#', '.', '.', '.'],
    ['#', '.', '#', '#', '#', '.', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '.', '#', '#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '#', '#', '#', '.', '.', '.'],
]

# Copiar mapa para edição
def reset_mapa():
    return [linha.copy() for linha in mapa_base]

# Mostrar mapa com legenda
def mostrar_mapa(mapa):
    print("\nMapa:")
    print("Legenda: S = início | G = objetivo | # = obstáculo | . = livre | P = caminho")
    for linha in mapa:
        print(' '.join(linha))
    print()

# Heurística Manhattan
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Vizinhos válidos
def get_neighbors(pos, mapa):
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    neighbors = []
    for d in dirs:
        nx, ny = pos[0] + d[0], pos[1] + d[1]
        if 0 <= nx < ROWS and 0 <= ny < COLS and mapa[nx][ny] != '#':
            neighbors.append((nx, ny))
    return neighbors

# Algoritmo A*
def a_star(start, goal, mapa):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstruir caminho
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for neighbor in get_neighbors(current, mapa):
            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f, neighbor))
    
    return None  # Sem caminho

# Entrada de coordenadas
def ler_coordenada(nome):
    while True:
        try:
            entrada = input(f"Digite as coordenadas de {nome} (linha coluna): ").split()
            linha, coluna = int(entrada[0]), int(entrada[1])
            if 0 <= linha < ROWS and 0 <= coluna < COLS:
                return (linha, coluna)
            else:
                print("Coordenadas fora do mapa. Tente novamente.")
        except:
            print("Entrada inválida. Use o formato: linha coluna (ex: 0 0)")

# Programa principal
def main():
    print("=== Algoritmo A* Interativo ===")
    print("Você pode escolher o ponto de início e objetivo no mapa.")
    mostrar_mapa(mapa_base)

    mapa = reset_mapa()

    start = ler_coordenada("início")
    while mapa[start[0]][start[1]] == '#':
        print("O ponto de início está em um obstáculo! Escolha outro.")
        start = ler_coordenada("início")

    goal = ler_coordenada("objetivo")
    while mapa[goal[0]][goal[1]] == '#':
        print("O ponto de objetivo está em um obstáculo! Escolha outro.")
        goal = ler_coordenada("objetivo")

    mapa[start[0]][start[1]] = 'S'
    mapa[goal[0]][goal[1]] = 'G'

    path = a_star(start, goal, mapa)

    if path:
        for r, c in path:
            if mapa[r][c] not in ('S', 'G'):
                mapa[r][c] = 'P'
        mostrar_mapa(mapa)
        print(f"Caminho encontrado com {len(path)} passos.")
    else:
        mostrar_mapa(mapa)
        print("❌ Caminho não encontrado.")

if __name__ == "__main__":
    main()
