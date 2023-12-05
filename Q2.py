def multiplicar_matrizes_quadradas(A, B):

  # Se as matrizes forem de tamanho 1, retorne a multiplicação dos elementos.
  if len(A) == 1:
    return A[0] * B[0]

  # Divida cada matriz em 9 submatrizes quadradas.
  A_submatrizes = dividir_matriz_quadrada(A)
  B_submatrizes = dividir_matriz_quadrada(B)

  # Calcule as 9 subprodutos.
  subprodutos = []
  for i in range(3):
    for j in range(3):
      subprodutos.append(
          multiplicar_matrizes_quadradas(A_submatrizes[i][j], B_submatrizes[j][i]))

  # Retorne a soma dos 9 subprodutos.
  return sum(subprodutos)

def dividir_matriz_quadrada(M):

  M_submatrizes = []
  for i in range(3):
    for j in range(3):
      M_submatrizes.append(M[i * 3:(i + 1) * 3, j * 3:(j + 1) * 3])
  return M_submatrizes
