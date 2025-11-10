def insertion_sort(bucket):
    """Insertion Sort otimizado para listas pequenas"""
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
    return bucket


def bucket_sort(arr):
    if len(arr) <= 1:
        return arr.copy()
    
    # Normaliza para [0, 1)
    min_val, max_val = min(arr), max(arr)
    if max_val == min_val:
        return arr.copy()
    
    n = len(arr)
    buckets = [[] for _ in range(n)]
    
    # 1. Distribui nos baldes
    for num in arr:
        normalized = (num - min_val) / (max_val - min_val)
        index = int(normalized * n)
        if index >= n:
            index = n - 1
        buckets[index].append(num)
    
    # 2. Ordena cada balde com INSERTION SORT
    for i in range(n):
        buckets[i] = insertion_sort(buckets[i])
    
    # 3. Concatena
    return [item for bucket in buckets for item in bucket]


# Teste
arr = [78, 17, 39, 26, 72, 94, 21, 12, 23, 68]
print("Original:", arr)
print("Ordenado:", bucket_sort(arr))