# a_estrela_ia.py
# Algoritmo A* Interativo – Seminário de Inteligência Artificial


Este projeto foi desenvolvido como parte de um **seminário de Inteligência Artificial** na disciplina de Computação da UFAL ministrada pelo professor Evandro, com foco na compreensão e implementação do algoritmo A*.

Este projeto implementa uma versão interativa do algoritmo A* (A-estrela) em Python, com um mapa fixo contendo obstáculos. O objetivo é demonstrar, de forma didática, como o algoritmo encontra o caminho ótimo entre dois pontos em um grid bidimensional.

## 📌 Objetivo

Apresentar o funcionamento do algoritmo A* no contexto da disciplina de **Inteligência Artificial**, explorando conceitos como:
- Busca heurística
- Heurística de Manhattan
- Reconstrução de caminho
- Manipulação de mapas com obstáculos

---

## 💡 Como funciona

O usuário deve informar as coordenadas de **início** e **objetivo**. O algoritmo então:
1. Verifica se os pontos estão em posições válidas (não são obstáculos).
2. Executa o A* para encontrar o caminho mais curto entre os dois pontos.
3. Mostra o mapa com a trajetória marcada e a quantidade de passos.

### Legenda do mapa:

| Símbolo | Significado       |
|---------|-------------------|
| `S`     | Ponto de início   |
| `G`     | Objetivo final    |
| `#`     | Obstáculo         |
| `.`     | Espaço livre      |
| `P`     | Caminho percorrido|

---

## 🚀 Como executar

1. Certifique-se de ter o Python 3 instalado.
2. Salve o código em um arquivo, por exemplo: `astar_interativo.py`.
3. Execute no terminal com:

```bash
python astar_interativo.py
```

4. Digite as coordenadas de início e objetivo quando solicitado.  
   Exemplo de entrada: `0 0` (linha 0, coluna 0)

---

## 🧠 Conceitos aplicados

- **Busca A\***: Algoritmo de busca informada que combina custo real (`g`) e custo estimado até o objetivo (`h`) para encontrar o caminho mais curto.
- **Heurística de Manhattan**: Soma das distâncias horizontais e verticais entre dois pontos, adequada para grids sem diagonais.
- **Estrutura de dados de fila de prioridade (`heapq`)**: Garante que o próximo nó a ser explorado é sempre o mais promissor (menor `f = g + h`).

---

## 🗺️ Exemplo de mapa

```
. . . . . . . . . .
. # # # # . # # # .
. . . . # . . . # .
. # # . # # # . # .
. . # . . . # . . .
# . # # # . # # # .
. . . . # . . . # .
. # # . # # # . # .
. . . . . . . . # .
. # # # # # # . . .
```

---

## 📚 Créditos

Este projeto foi desenvolvido como parte de um **seminário de Inteligência Artificial** na disciplina de Computação da UFAL, com foco na compreensão e implementação do algoritmo A*.
