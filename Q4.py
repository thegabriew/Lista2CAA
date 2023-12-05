from typing import List

def elemento_majoritario(nums: List[int]) -> int:

  # Inicializa o contador do elemento majoritário e o índice do candidato.
  contador = 0
  candidato = nums[0]

  # Percorre o array.
  for número in nums:
    # Se o número atual for igual ao candidato, incrementa o contador.
    if número == candidato:
      contador += 1
    # Se o número atual for diferente do candidato, decrementa o contador.
    else:
      contador -= 1

    # Se o contador for negativo, o candidato não é o elemento majoritário.
    if contador < 0:
      # Atualiza o candidato e o contador.
      candidato = número
      contador = 1

  # Retorna o candidato.
  return candidato
