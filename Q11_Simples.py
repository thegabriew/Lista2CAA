from typing import List, Tuple

def merge_sorted_arrays(nums1, m, nums2, n):
  
  # Inicialize o índice dos dois arrays.

  i = 0
  j = 0

  # Percorra os dois arrays, comparando os elementos.

  while i < m and j < n:
    if nums1[i] <= nums2[j]:
      nums1[i + j] = nums1[i]
      i += 1
    else:
      nums1[i + j] = nums2[j]
      j += 1

  # Adicione os elementos restantes do primeiro array, se houver.

  while i < m:
    nums1[i + j] = nums1[i]
    i += 1

  # Adicione os elementos restantes do segundo array, se houver.

  while j < n:
    nums1[i + j] = nums2[j]
    j += 1

