def max_palindrome(sequencia):

    # Obtém o tamanho da sequência.
    n = len(sequencia)

    # Inicializa uma matriz booleana dp de tamanho n x n.
    dp = [[False] * n for _ in range(n)]

    # Preenche a matriz dp.
    for i in range(n):
        dp[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if length == 2 and sequencia[i] == sequencia[j]:
                dp[i][j] = True
            elif sequencia[i] == sequencia[j] and dp[i + 1][j - 1]:
                dp[i][j] = True

    # Encontra o tamanho e o índice do início da subsequência palíndroma de tamanho máximo.
    tamanho_maximo = 0
    inicio_maximo = 0
    for i in range(n):
        for j in range(i, n):
            if dp[i][j] and tamanho_maximo < j - i + 1:
                tamanho_maximo = j - i + 1
                inicio_maximo = i

    # Retorna a subsequência palíndroma de tamanho máximo.
    return sequencia[inicio_maximo:inicio_maximo + tamanho_maximo]


# Exemplo de uso:
sequencia = "babad"
resultado = max_palindrome(sequencia)
print(resultado)
