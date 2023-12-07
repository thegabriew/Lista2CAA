from typing import List, Tuple

def particao_de_tres_vias(S: List[int], pivo: int, p: int,
                          r: int) -> Tupla[int, int]:

    # Inicializa os ponteiros esquerdo e direito.
    indice_esquerdo = p
    indice_direito = r

    # Percorre o array até que os ponteiros se encontrem.
    while indice_esquerdo <= indice_direito:
        # Enquanto o elemento atual for menor que o pivô, mova-o para a esquerda.
        while S[indice_esquerdo] < pivo:
            indice_esquerdo += 1

        # Enquanto o elemento atual for maior que o pivô, mova-o para a direita.
        while S[indice_direito] > pivo:
            indice_direito -= 1

        # Se os ponteiros ainda não se encontraram, troque os dois elementos.
        if indice_esquerdo <= indice_direito:
            S[indice_esquerdo], S[indice_direito] = S[indice_direito], S[indice_esquerdo]
            indice_esquerdo += 1
            indice_direito -= 1

    # Retorne os índices `q1` e `q2`.
    return indice_esquerdo, indice_direito
