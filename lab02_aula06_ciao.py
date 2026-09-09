import numpy as np
import random
import matplotlib.pyplot as plt

CUSTOS = np.array([
    [0, 2, 4, np.inf, np.inf, np.inf],
    [2, 0, 1, 5, np.inf, np.inf],
    [4, 1, 0, 2, 3, np.inf],
    [np.inf, 5, 2, 0, 1, 4],
    [np.inf, np.inf, 3, 1, 0, 2],
    [np.inf, np.inf, np.inf, 4, 2, 0]
])

ORIGEM = 0
DESTINO = 5

NUM_FORMIGAS = 20
NUM_ITERACOES = 50

ALPHA = 1.0
BETA = 2.0

TAXA_EVAPORACAO = 0.5
Q = 100


def executar_aco():

    feromonio = np.ones_like(CUSTOS, dtype=float)
    feromonio[CUSTOS == np.inf] = 0

    def obter_vizinhos(no):

        return [
            proximo
            for proximo in range(len(CUSTOS))
            if proximo != no
            and CUSTOS[no][proximo] != np.inf
        ]


    def escolher_proximo(no_atual, visitados):

        candidatos = [
            no for no in obter_vizinhos(no_atual)
            if no not in visitados
        ]

        if not candidatos:
            return None

        atratividades = []

        for proximo in candidatos:

            fer = feromonio[no_atual][proximo]
            custo = CUSTOS[no_atual][proximo]

            atratividade = (
                fer ** ALPHA
                * (1 / custo) ** BETA
            )

            atratividades.append(atratividade)

        soma = sum(atratividades)

        probabilidades = [
            valor / soma
            for valor in atratividades
        ]

        return random.choices(
            candidatos,
            weights=probabilidades,
            k=1
        )[0]


    def construir_rota():

        rota = [ORIGEM]
        atual = ORIGEM

        while atual != DESTINO:

            proximo = escolher_proximo(
                atual,
                rota
            )

            if proximo is None:
                return None

            rota.append(proximo)
            atual = proximo

        return rota


    def calcular_custo(rota):

        total = 0

        for i in range(len(rota) - 1):
            total += CUSTOS[
                rota[i],
                rota[i + 1]
            ]

        return total


    def evaporar_feromonio():

        nonlocal feromonio

        feromonio *= (1 - TAXA_EVAPORACAO)

        feromonio[CUSTOS == np.inf] = 0


    def depositar_feromonio(rota, custo):

        deposito = Q / custo

        for i in range(len(rota) - 1):

            origem = rota[i]
            destino = rota[i + 1]

            feromonio[origem][destino] += deposito


    melhor_rota = None
    melhor_custo = float("inf")
    historico = []

    for iteracao in range(NUM_ITERACOES):

        rotas = []

        for _ in range(NUM_FORMIGAS):

            rota = construir_rota()

            if rota is not None:

                custo = calcular_custo(rota)

                rotas.append((rota, custo))

                if custo < melhor_custo:

                    melhor_custo = custo
                    melhor_rota = rota.copy()

        evaporar_feromonio()

        for rota, custo in rotas:

            depositar_feromonio(
                rota,
                custo
            )

        historico.append(melhor_custo)

    return melhor_rota, melhor_custo, historico


experimentos = [
    ("ALPHA = 1.0", 1.0, 2.0, 0.5, 20),
    ("ALPHA = 0.1", 0.1, 2.0, 0.5, 20),
    ("ALPHA = 5.0", 5.0, 2.0, 0.5, 20),

    ("BETA = 0.5", 1.0, 0.5, 0.5, 20),
    ("BETA = 5.0", 1.0, 5.0, 0.5, 20),

    ("EVAPORAÇÃO = 0.1", 1.0, 2.0, 0.1, 20),
    ("EVAPORAÇÃO = 0.9", 1.0, 2.0, 0.9, 20),

    ("FORMIGAS = 5", 1.0, 2.0, 0.5, 5),
    ("FORMIGAS = 50", 1.0, 2.0, 0.5, 50)
]


for nome, alpha, beta, evaporacao, formigas in experimentos:

    ALPHA = alpha
    BETA = beta
    TAXA_EVAPORACAO = evaporacao
    NUM_FORMIGAS = formigas

    rota, custo, historico = executar_aco()

    print("\n========== RESULTADO DO EXPERIMENTO ==========")
    print("Experimento:", nome)
    print("Número de formigas:", NUM_FORMIGAS)
    print("Número de iterações:", NUM_ITERACOES)
    print("ALPHA:", ALPHA)
    print("BETA:", BETA)
    print("Taxa de evaporação:", TAXA_EVAPORACAO)
    print("Melhor rota:", rota)
    print("Melhor custo:", custo)

    plt.figure(figsize=(8, 4))
    plt.plot(historico)
    plt.xlabel("Iteração")
    plt.ylabel("Melhor custo")
    plt.title(nome)
    plt.grid()
    plt.show()
