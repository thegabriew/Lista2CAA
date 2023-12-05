from typing import List

def squares_of_sorted_array(nums: List[int]) -> List[int]:
    # Usa list comprehension para calcular os quadrados e armazená-los em um novo vetor.
    squares = [num * num for num in nums]
    
    # Ordena o vetor resultante em ordem não decrescente.
    squares.sort()

    # Retorna o vetor ordenado.
    return squares
