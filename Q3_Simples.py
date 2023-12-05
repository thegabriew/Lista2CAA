def find_two_sum(nums, X):
  
  # Percorre todos os elementos do vetor.
  for i in range(len(nums)):
    # Percorre todos os elementos restantes do vetor.
    for j in range(i + 1, len(nums)):
      # Se a soma dos dois números for igual a X, retorna os índices.
      if nums[i] + nums[j] == X:
        return [i, j]
  # Se não for encontrado nenhum par de números, retorna None.
  return None
