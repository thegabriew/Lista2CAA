def quadrados_ordenados(nums: List[int]) -> List[int]:

  # Cria um novo array para armazenar os quadrados.
  quadrados = [0] * len(nums)

  # Percorre o array original.
  for i in range(len(nums)):
    # Quadra o número atual.
    quadrados[i] = nums[i] ** 2

  # Ordena o array dos quadrados.
  quadrados.sort()

  # Retorna o array dos quadrados ordenados.
  return quadrados
