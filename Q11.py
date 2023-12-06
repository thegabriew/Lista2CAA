def merge_sorted_arrays_in_place(nums1: List[int], m: int, nums2: List[int],
                                 n: int) -> None:

  # Inicializa os ponteiros para os dois arrays.
  i = 0
  j = 0

  # Percorre os dois arrays, mantendo um ponteiro para o menor elemento.
  while i < m and j < n:
    if nums1[i] < nums2[j]:
      # O elemento atual de `nums1` é menor. Insira-o em `nums1`.
      nums1[i + j] = nums1[i]
      i += 1
    else:
      # O elemento atual de `nums2` é menor ou igual. Insira-o em `nums1`.
      nums1[i + j] = nums2[j]
      j += 1

  # Se `i` ainda não chegou ao final de `nums1`, insira os elementos restantes de `nums1`
  # em `nums1`.
  while i < m:
    nums1[i + j] = nums1[i]
    i += 1

  # Se `j` ainda não chegou ao final de `nums2`, insira os elementos restantes de `nums2`
  # em `nums1`.
  while j < n:
    nums1[i + j] = nums2[j]
    j += 1
