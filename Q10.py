def encontrar_posicao_insercao(nums: List[int], alvo: int) -> int:
    # Inicializa os ponteiros esquerdo e direito.
  esquerda = 0
  direita = len(nums) - 1

  # Percorre o array até que os ponteiros se encontrem.
  while esquerda <= direita:
    # Calcula o meio do array.
    meio = (esquerda + direita) // 2

    # Se o alvo for igual ao elemento no meio, retorna o índice do meio.
    if nums[meio] == alvo:
      return meio

    # Se o alvo for menor que o elemento no meio, atualiza o ponteiro esquerdo.
    elif nums[meio] > alvo:
      direita = meio - 1

    # Se o alvo for maior que o elemento no meio, atualiza o ponteiro direito.
    else:
      esquerda = meio + 1

  # Se o loop terminar e os ponteiros ainda não se encontrarem, o alvo não está no array.
  # Nesse caso, retorna o índice onde o alvo seria inserido.
  return esquerda
```