def encontrar_dois_soma(números, X):

  # Ordena o vetor.
  números.sort()

  # Percorre sobre todos os elementos do vetor.
  for índice_1 in range(len(números)):
    # Usa a busca binária para encontrar o complemento de números[índice_1] no vetor.
    índice_2 = bisect.bisect_left(números, X - números[índice_1])

    # Se o complemento for encontrado, retorna os índices.
    if índice_2 != len(números) and números[índice_2] == X - números[índice_1]:
      return [índice_1, índice_2]

  # Se não for encontrado nenhum par de números, retorna None.
  return None
