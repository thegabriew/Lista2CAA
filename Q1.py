def three_way_partition(S: List[int], piv: int, p: int,
                        r: int) -> Tuple[int, int]:

  # Inicializa os ponteiros esquerdo e direito.
  i = p
  j = r

  # Percorre o array até que os ponteiros se encontrem.
  while i <= j:
    # Enquanto o elemento atual for menor que o pivô, mova-o para a esquerda.
    while S[i] < piv:
      i += 1

    # Enquanto o elemento atual for maior que o pivô, mova-o para a direita.
    while S[j] > piv:
      j -= 1

    # Se os ponteiros ainda não se encontraram, troque os dois elementos.
    if i <= j:
      S[i], S[j] = S[j], S[i]
      i += 1
      j -= 1

  # Retorne os índices `q1` e `q2`.
  return i, j
