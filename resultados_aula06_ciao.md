Resultado LAB 01:

Matriz inicial de feromônio:
[[1. 1. 1. 0. 0. 0.]
 [1. 1. 1. 1. 0. 0.]
 [1. 1. 1. 1. 1. 0.]
 [0. 1. 1. 1. 1. 1.]
 [0. 0. 1. 1. 1. 1.]
 [0. 0. 0. 1. 1. 1.]]
Vizinhos do nó 0: [1, 2]
Vizinhos do nó 2: [0, 1, 3, 4]

Rotas encontradas:
Formiga 1: [0, 1, 2, 3, 4, 5]
Formiga 2: [0, 1, 2, 4, 5]
Formiga 3: [0, 1, 2, 4, 3, 5]
Formiga 4: [0, 2, 1, 3, 4, 5]
Formiga 5: [0, 1, 2, 3, 4, 5]

Rota: [0, 1, 2, 3, 4, 5]
Custo: 8.0

========== RESULTADO ==========
Melhor rota encontrada: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0

Matriz final de feromônio:
[[8.88178420e-16 5.00000000e+02 6.27570171e-14 0.00000000e+00
  0.00000000e+00 0.00000000e+00]
 [8.88178420e-16 8.88178420e-16 5.00000000e+02 6.05141423e-14
  0.00000000e+00 0.00000000e+00]
 [8.88178420e-16 2.82167452e-14 8.88178420e-16 5.00000000e+02
  4.75929060e-13 0.00000000e+00]
 [0.00000000e+00 8.88178420e-16 8.88178420e-16 8.88178420e-16
  5.00000000e+02 4.78620510e-13]
 [0.00000000e+00 0.00000000e+00 8.88178420e-16 3.87111219e-13
  8.88178420e-16 5.00000000e+02]
 [0.00000000e+00 0.00000000e+00 0.00000000e+00 8.88178420e-16
  8.88178420e-16 8.88178420e-16]]

<img width="457" height="502" alt="image" src="https://github.com/user-attachments/assets/f68d368a-451a-4c28-9a30-e32dab85a572" />

1. Por que o ACO utiliza várias formigas em vez de apenas uma formiga procurando a melhor rota? Explique qual é a importância de explorar diferentes caminhos.
R: Várias formigas: permitem explorar diferentes caminhos e aumentam as chances de encontrar uma boa solução.

2. Por que uma rota de menor custo recebe mais feromônio? Explique como essa regra influencia o comportamento das próximas formigas.
R:Mais feromônio nas melhores rotas: rotas de menor custo são melhores, então recebem mais feromônio e ficam mais atrativas.

3. O que poderia acontecer se não existisse evaporação do feromônio? Explique por que manter para sempre as primeiras informações encontradas poderia prejudicar a busca por soluções melhores.
R:Sem evaporação: o algoritmo poderia ficar preso em caminhos antigos e deixar de explorar soluções melhores.

----------------   -----------------  ----------------

Resultado LAB 02:

========== RESULTADO DO EXPERIMENTO ==========
Experimento: ALPHA = 1.0
Número de formigas: 20
Número de iterações: 50
ALPHA: 1.0
BETA: 2.0
Taxa de evaporação: 0.5
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0
<img width="351" height="202" alt="image" src="https://github.com/user-attachments/assets/8686a463-5c78-4106-9336-26465b49fb8d" />


========== RESULTADO DO EXPERIMENTO ==========
Experimento: ALPHA = 0.1
Número de formigas: 20
Número de iterações: 50
ALPHA: 0.1
BETA: 2.0
Taxa de evaporação: 0.5
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0
<img width="350" height="202" alt="image" src="https://github.com/user-attachments/assets/e231e9d0-7f78-48c8-84e0-f228845e8a6d" />


========== RESULTADO DO EXPERIMENTO ==========
Experimento: ALPHA = 5.0
Número de formigas: 20
Número de iterações: 50
ALPHA: 5.0
BETA: 2.0
Taxa de evaporação: 0.5
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0
<img width="347" height="199" alt="image" src="https://github.com/user-attachments/assets/30d450e2-e971-49b9-b647-8707161c4fe7" />


========== RESULTADO DO EXPERIMENTO ==========
Experimento: BETA = 0.5
Número de formigas: 20
Número de iterações: 50
ALPHA: 1.0
BETA: 0.5
Taxa de evaporação: 0.5
Melhor rota: [0, 1, 2, 4, 5]
Melhor custo: 8.0
<img width="347" height="198" alt="image" src="https://github.com/user-attachments/assets/88153c16-6a8d-4af5-8fe1-2eef7a2bc1b7" />


========== RESULTADO DO EXPERIMENTO ==========
Experimento: BETA = 5.0
Número de formigas: 20
Número de iterações: 50
ALPHA: 1.0
BETA: 5.0
Taxa de evaporação: 0.5
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0
<img width="350" height="203" alt="image" src="https://github.com/user-attachments/assets/c4496f42-1290-40f3-9929-84e076e252f7" />


========== RESULTADO DO EXPERIMENTO ==========
Experimento: EVAPORAÇÃO = 0.1
Número de formigas: 20
Número de iterações: 50
ALPHA: 1.0
BETA: 2.0
Taxa de evaporação: 0.1
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0
<img width="350" height="202" alt="image" src="https://github.com/user-attachments/assets/7f38038b-5b68-40db-871c-e52885bc2750" />


========== RESULTADO DO EXPERIMENTO ==========
Experimento: EVAPORAÇÃO = 0.9
Número de formigas: 20
Número de iterações: 50
ALPHA: 1.0
BETA: 2.0
Taxa de evaporação: 0.9
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0
<img width="350" height="205" alt="image" src="https://github.com/user-attachments/assets/e1434de9-d14b-4aa9-8624-9fd2b2b4d568" />


========== RESULTADO DO EXPERIMENTO ==========
Experimento: FORMIGAS = 5
Número de formigas: 5
Número de iterações: 50
ALPHA: 1.0
BETA: 2.0
Taxa de evaporação: 0.5
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0
<img width="350" height="202" alt="image" src="https://github.com/user-attachments/assets/75239b82-05c0-46e6-a893-9c521266df5d" />


========== RESULTADO DO EXPERIMENTO ==========
Experimento: FORMIGAS = 50
Número de formigas: 50
Número de iterações: 50
ALPHA: 1.0
BETA: 2.0
Taxa de evaporação: 0.5
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0
<img width="348" height="200" alt="image" src="https://github.com/user-attachments/assets/b155e545-e592-4c24-9aab-e6f7d9f9a0b4" />

1. Quando aumentamos o ALPHA, a influência da experiência acumulada pelas formigas aumenta ou diminui?
R: Aumenta, pois o feromônio passa a ter maior influência na escolha dos caminhos.

2. O que acontece quando o BETA é aumentado?
R: Caminhos de menor custo ficam mais atrativos.

3. O que acontece quando a evaporação aumenta?
R: O algoritmo esquece as experiências antigas mais rapidamente e explora mais novas possibilidades.

4. O que acontece quando aumentamos o número de formigas?
R: Mais caminhos são explorados, aumentando a diversidade da busca.

----------------   -----------------  ----------------

Resultado LAB 03:

========== RESULTADO ==========
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0

Matriz final de feromônio:
[[8.88178420e-16 5.00000000e+02 4.79540434e-14 0.00000000e+00
  0.00000000e+00 0.00000000e+00]
 [8.88178420e-16 8.88178420e-16 5.00000000e+02 4.09050083e-14
  0.00000000e+00 0.00000000e+00]
 [8.88178420e-16 2.82167452e-14 8.88178420e-16 5.00000000e+02
  4.58738386e-14 0.00000000e+00]
 [0.00000000e+00 8.88178420e-16 1.35764416e-14 8.88178420e-16
  5.00000000e+02 7.26601719e-14]
 [0.00000000e+00 0.00000000e+00 8.88178420e-16 3.31855755e-14
  8.88178420e-16 5.00000000e+02]
 [0.00000000e+00 0.00000000e+00 0.00000000e+00 8.88178420e-16
  8.88178420e-16 8.88178420e-16]]

1. Por que a fórmula da atratividade utiliza 1 / custo em vez de utilizar diretamente o custo?
R: Para que caminhos de menor custo tenham maior atratividade.

2. O que acontece com a atratividade quando uma rota recebe mais feromônio?
R: A atratividade aumenta e o caminho tem maior chance de ser escolhido.

3. Por que a função construir_rota() precisa impedir que a formiga visite novamente um nó que já está na rota?
R: Para evitar ciclos e permitir a construção de uma rota válida.

  ----------------   -----------------  ----------------

Resultado LAB 04:

  ========== RESULTADO ==========

Melhor rota encontrada:
[0, 1, 2, 3, 4, 5]

Melhor custo:
8.0

Matriz final de feromônio:
[[8.88178420e-16 5.00000000e+02 2.02125008e-12 0.00000000e+00
  0.00000000e+00 0.00000000e+00]
 [8.88178420e-16 8.88178420e-16 5.00000000e+02 7.99458180e-14
  0.00000000e+00 0.00000000e+00]
 [8.88178420e-16 6.72575548e-14 8.88178420e-16 5.00000000e+02
  3.77577463e-12 0.00000000e+00]
 [0.00000000e+00 8.88178420e-16 1.35764416e-14 8.88178420e-16
  5.00000000e+02 4.28187868e-13]
 [0.00000000e+00 0.00000000e+00 8.88178420e-16 3.23862149e-13
  8.88178420e-16 5.00000000e+02]
 [0.00000000e+00 0.00000000e+00 0.00000000e+00 8.88178420e-16
  8.88178420e-16 8.88178420e-16]]
<img width="427" height="239" alt="image" src="https://github.com/user-attachments/assets/b4a07d78-fe6c-4e50-a8af-1ea788011041" />

1. Explique como o feromônio ajuda o ACO a aprender quais caminhos são melhores.
R: O feromônio funciona como uma memória coletiva, reforçando os caminhos de boas soluções.

2. Qual é a diferença entre explorar novos caminhos e aproveitar caminhos que já demonstraram ser bons?
R: Explorar é testar caminhos novos; aproveitar é utilizar caminhos que já apresentaram bons resultados.

3. Se você precisasse melhorar o desempenho desse ACO para uma rede muito maior, qual parâmetro ou parte do algoritmo investigaria primeiro?
R: Eu investigaria o número de formigas, o número de iterações e os parâmetros ALPHA e BETA para equilibrar exploração e aproveitamento.
