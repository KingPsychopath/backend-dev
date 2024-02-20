from collections import defaultdict

def findMaxFrequency(x, y, z, arr):
    frequency = defaultdict(int)
    
    for num in arr:
        frequency[num] += 1
        frequency[num + x] += 1
        frequency[num - y] += 1
        frequency[num * z] += 1

    # For each number, only keep the maximum frequency among the original and the three operations
    for num in arr:
        max_freq = max(frequency[num], frequency[num + x], frequency[num - y], frequency[num * z])
        frequency[num] = max_freq
        frequency[num + x] = max_freq
        frequency[num - y] = max_freq
        frequency[num * z] = max_freq

    max_frequency = max(frequency.values())
    return max_frequency

print(findMaxFrequency(2, 2, 1, [10, 5, 5, 2, 11]))  # Expected output: 2
print(findMaxFrequency(237, 98808, 1, [49559]))  # Expected output: 1