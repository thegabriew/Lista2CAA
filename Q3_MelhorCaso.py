from typing import List, Tuple

def dois_soma(números: List[int], alvo: int) -> List[int]:

  # Cria um dicionário para armazenar os números já vistos.
  vistos = {}

  # Percorre o vetor `números`.
  for índice, número in enumerate(números):
    # Verifica se o número `alvo - número` já foi visto.
    alvo_complemento = alvo - número
    if alvo_complemento in vistos:
      # Retorna os índices dos dois números.
      return [vistos[alvo_complemento], índice]
    else:
      # Armazena o número `número` no dicionário.
      vistos[número] = índice

  # Se chegar aqui, significa que não encontrou uma solução.
  return None
